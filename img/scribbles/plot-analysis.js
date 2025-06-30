// Plot Analysis Module for Plot Line Tracer
// This file handles the generation of plots and tables based on traced lines

(function() {
    'use strict';

    // Wait for the main PlotTracer object to be available
    function initializeAnalysis() {
        if (!window.PlotTracer) {
            setTimeout(initializeAnalysis, 100);
            return;
        }

        console.log('Plot Analysis Module Initialized');

        // Override the onLinesChanged function to auto-update
        window.PlotTracer.onLinesChanged = function() {
            console.log('Lines changed:', window.PlotTracer.allLines.length, 'lines');
            updatePlotAndTable();
        };
    }

    function updatePlotAndTable() {
        const allLines = window.PlotTracer.allLines;
        const plotContainer = document.getElementById('plotContainer');
        const tableContainer = document.getElementById('tableContainer');

        if (allLines.length === 0) {
            plotContainer.innerHTML = '<div class="placeholder">No lines to plot</div>';
            tableContainer.innerHTML = '<div class="placeholder">No data to display</div>';
            return;
        }

        // Generate CDF plot
        generateCDFPlot(allLines, plotContainer);

        // Generate the percentile analysis table
        generatePercentileTable(allLines, tableContainer);
    }

    function generateCDFPlot(allLines, container) {
        // Define the y-thresholds we're interested in
        const thresholds = [
            { y: 6.4199, label: '1 month', color: '#FF6B6B' },
            { y: 7.4991, label: '1 year', color: '#4ECDC4' },
            { y: 8.4991, label: '10 year', color: '#45B7D1' }
        ];

        // Calculate crossing data for each threshold
        const cdfData = {};
        let minYear = Infinity;
        let maxYear = -Infinity;

        thresholds.forEach(threshold => {
            const crossingYears = [];

            // Find crossing years for each line
            allLines.forEach(line => {
                let crossingX = findYCrossing(line.points, threshold.y);

                // Special handling for 10-year threshold (8.4991)
                if (crossingX === null && threshold.y === 8.4991) {
                    crossingX = extrapolateToThreshold(line.points, threshold.y);
                }

                if (crossingX !== null) {
                    crossingYears.push(crossingX);
                    minYear = Math.min(minYear, crossingX);
                    maxYear = Math.max(maxYear, crossingX);
                }
            });

            // Sort crossing years
            crossingYears.sort((a, b) => a - b);

            cdfData[threshold.label] = {
                years: crossingYears,
                color: threshold.color
            };
        });

        // Set up responsive plot dimensions
        const containerWidth = container.clientWidth - 20; // Account for padding
        const width = Math.min(800, containerWidth);
        const height = Math.min(400, width * 0.5); // Maintain aspect ratio
        const margin = { top: 30, right: 150, bottom: 60, left: 80 };
        const plotWidth = width - margin.left - margin.right;
        const plotHeight = height - margin.top - margin.bottom;

        // Create canvas
        container.innerHTML = `<canvas id="cdfCanvas" width="${width}" height="${height}" style="display: block; margin: 0 auto; max-width: 100%;"></canvas>`;
        const canvas = document.getElementById('cdfCanvas');
        const ctx = canvas.getContext('2d');

        // Clear canvas
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, width, height);

        // Set up scales
        const xMin = Math.floor(minYear / 5) * 5; // Round down to nearest 5
        const xMax = Math.ceil(Math.max(maxYear, 2050) / 5) * 5; // Round up to nearest 5
        const xScale = (year) => margin.left + ((year - xMin) / (xMax - xMin)) * plotWidth;
        const yScale = (percent) => margin.top + plotHeight - (percent / 100) * plotHeight;

        // Draw axes
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 2;

        // X-axis
        ctx.beginPath();
        ctx.moveTo(margin.left, margin.top + plotHeight);
        ctx.lineTo(margin.left + plotWidth, margin.top + plotHeight);
        ctx.stroke();

        // Y-axis
        ctx.beginPath();
        ctx.moveTo(margin.left, margin.top);
        ctx.lineTo(margin.left, margin.top + plotHeight);
        ctx.stroke();

        // Draw grid lines and labels
        ctx.strokeStyle = '#e0e0e0';
        ctx.lineWidth = 1;
        ctx.font = '12px Montserrat, sans-serif';
        ctx.fillStyle = '#666';
        ctx.textAlign = 'center';

        // X-axis grid and labels
        for (let year = xMin; year <= xMax; year += 10) {
            const x = xScale(year);

            // Grid line
            ctx.beginPath();
            ctx.moveTo(x, margin.top);
            ctx.lineTo(x, margin.top + plotHeight);
            ctx.stroke();

            // Label
            ctx.fillText(year, x, margin.top + plotHeight + 20);
        }

        // Y-axis grid and labels
        ctx.textAlign = 'right';
        for (let percent = 0; percent <= 100; percent += 20) {
            const y = yScale(percent);

            // Grid line
            ctx.beginPath();
            ctx.moveTo(margin.left, y);
            ctx.lineTo(margin.left + plotWidth, y);
            ctx.stroke();

            // Label
            ctx.fillText(percent + '%', margin.left - 10, y + 4);
        }

        // Draw CDF curves
        ctx.lineWidth = 2;

        thresholds.forEach(threshold => {
            const data = cdfData[threshold.label];
            if (data.years.length === 0) return;

            ctx.strokeStyle = data.color;
            ctx.beginPath();

            // Start from 0%
            ctx.moveTo(xScale(xMin), yScale(0));

            // Draw the CDF
            data.years.forEach((year, index) => {
                const percentage = ((index + 1) / allLines.length) * 100;

                // Draw horizontal line to this year
                ctx.lineTo(xScale(year), yScale(percentage - 100 / allLines.length));

                // Draw vertical line to new percentage
                ctx.lineTo(xScale(year), yScale(percentage));
            });

            // Extend to the right edge at final percentage
            const finalPercentage = (data.years.length / allLines.length) * 100;
            ctx.lineTo(xScale(xMax), yScale(finalPercentage));

            ctx.stroke();
        });

        // Draw legend
        const legendX = margin.left + plotWidth + 20;
        let legendY = margin.top + 20;

        ctx.font = '600 14px Montserrat, sans-serif';
        ctx.fillStyle = '#333';
        ctx.textAlign = 'left';
        ctx.fillText('Thresholds:', legendX, legendY);

        legendY += 25;
        ctx.font = '12px Montserrat, sans-serif';

        thresholds.forEach(threshold => {
            // Color box
            ctx.fillStyle = threshold.color;
            ctx.fillRect(legendX, legendY - 10, 15, 12);

            // Label
            ctx.fillStyle = '#333';
            ctx.fillText(threshold.label, legendX + 20, legendY);

            legendY += 20;
        });

        // Add vertical line at 2050
        ctx.strokeStyle = '#FF5722';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(xScale(2050), margin.top);
        ctx.lineTo(xScale(2050), margin.top + plotHeight);
        ctx.stroke();
        ctx.setLineDash([]);

        // Label for 2050 line
        ctx.fillStyle = '#FF5722';
        ctx.font = '11px Montserrat, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('2050', xScale(2050), margin.top - 5);

        // Axis labels
        ctx.fillStyle = '#333';
        ctx.font = '600 14px Montserrat, sans-serif';

        // X-axis label
        ctx.textAlign = 'center';
        ctx.fillText('Year', margin.left + plotWidth / 2, height - 15);

        // Y-axis label
        ctx.save();
        ctx.translate(15, margin.top + plotHeight / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText('Chance of reaching threshold', 0, 0);
        ctx.restore();

        // Title
        ctx.font = '600 16px Montserrat, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Scribble-based AI forecasting', width / 2, 20);
    }

    function generatePercentileTable(allLines, container) {
        // Define the y-thresholds we're interested in
        const thresholds = [
            { y: 6.4199, label: '1 month' },
            { y: 7.4991, label: '1 year' },
            { y: 8.4991, label: '10 year' }
        ];

        // Calculate crossing points for each threshold
        const crossingData = {};

        thresholds.forEach(threshold => {
            crossingData[threshold.label] = {
                y: threshold.y,
                crossingXValues: []
            };

            // For each line, find where it crosses this y-threshold
            allLines.forEach((line, lineIndex) => {
                let crossingX = findYCrossing(line.points, threshold.y);

                // Special handling for 10-year threshold (8.4991)
                if (crossingX === null && threshold.y === 8.4991) {
                    crossingX = extrapolateToThreshold(line.points, threshold.y);
                }

                if (crossingX !== null) {
                    crossingData[threshold.label].crossingXValues.push({
                        x: crossingX,
                        lineIndex: lineIndex + 1,
                        color: line.color
                    });
                }
            });
        });

        // Generate the HTML table
        let html = '<h4>Percentile Analysis of Threshold Crossings</h4>';
        html += '<table style="width: 100%; border-collapse: collapse; font-size: 14px; margin-bottom: 20px;">';
        html += '<thead>';
        html += '<tr style="background-color: #e3f2fd;">';
        html += '<th style="padding: 10px; border: 1px solid #ddd; text-align: left;">Threshold</th>';
        html += '<th style="padding: 10px; border: 1px solid #ddd; text-align: center;">10th Percentile<br>(Year)</th>';
        html += '<th style="padding: 10px; border: 1px solid #ddd; text-align: center;">50th Percentile<br>(Median Year)</th>';
        html += '<th style="padding: 10px; border: 1px solid #ddd; text-align: center;">90th Percentile<br>(Year)</th>';
        html += '<th style="padding: 10px; border: 1px solid #ddd; text-align: center;">% Reached<br>by 2050</th>';
        html += '</tr>';
        html += '</thead>';
        html += '<tbody>';

        thresholds.forEach(threshold => {
            const data = crossingData[threshold.label];
            const xValues = data.crossingXValues.map(item => item.x).sort((a, b) => a - b);

            let p10 = '-';
            let p50 = '-';
            let p90 = '-';

            if (xValues.length > 0) {
                p10 = calculatePercentile(xValues, 0.10).toFixed(1);
                p50 = calculatePercentile(xValues, 0.50).toFixed(1);
                p90 = calculatePercentile(xValues, 0.90).toFixed(1);
            }

            // Calculate percentage that reached threshold by 2050
            const reachedBy2050 = xValues.filter(x => x <= 2050).length;
            const percentageReached = allLines.length > 0 ? 
                ((reachedBy2050 / allLines.length) * 100).toFixed(0) : '0';

            html += '<tr>';
            html += `<td style="padding: 10px; border: 1px solid #ddd; font-weight: bold;">${threshold.label}</td>`;
            html += `<td style="padding: 10px; border: 1px solid #ddd; text-align: center;">${p10}</td>`;
            html += `<td style="padding: 10px; border: 1px solid #ddd; text-align: center; font-weight: bold;">${p50}</td>`;
            html += `<td style="padding: 10px; border: 1px solid #ddd; text-align: center;">${p90}</td>`;
            html += `<td style="padding: 10px; border: 1px solid #ddd; text-align: center;">${percentageReached}%</td>`;
            html += '</tr>';
        });

        html += '</tbody>';
        html += '</table>';

        container.innerHTML = html;
    }

    // Find where a line crosses a specific y-value using linear interpolation
    function findYCrossing(points, targetY) {
        // Sort points by x-coordinate to ensure proper ordering
        const sortedPoints = [...points].sort((a, b) => a.plotX - b.plotX);

        for (let i = 0; i < sortedPoints.length - 1; i++) {
            const p1 = sortedPoints[i];
            const p2 = sortedPoints[i + 1];

            // Check if the target y is between these two points
            if ((p1.plotY <= targetY && p2.plotY >= targetY) || 
                (p1.plotY >= targetY && p2.plotY <= targetY)) {

                // Linear interpolation to find the x-coordinate
                const t = (targetY - p1.plotY) / (p2.plotY - p1.plotY);
                const crossingX = p1.plotX + t * (p2.plotX - p1.plotX);

                return crossingX;
            }
        }

        // No crossing found
        return null;
    }

    // Extrapolate to find when line would reach threshold
    function extrapolateToThreshold(points, targetY) {
        if (points.length < 2) return null;

        // Sort points by x-coordinate
        const sortedPoints = [...points].sort((a, b) => a.plotX - b.plotX);

        // Get the last point
        const lastPoint = sortedPoints[sortedPoints.length - 1];

        // Only extrapolate if the last point is above 8.4 but below the threshold
        if (lastPoint.plotY <= 8.4 || lastPoint.plotY >= targetY) {
            return null;
        }

        // Find the best two points for extrapolation (last two points with sufficient y-change)
        let p1 = null;
        let p2 = lastPoint;

        for (let i = sortedPoints.length - 2; i >= 0; i--) {
            if (Math.abs(sortedPoints[i].plotY - p2.plotY) > 0.1) {
                p1 = sortedPoints[i];
                break;
            }
        }

        if (!p1) return null;

        // Calculate slope
        const slope = (p2.plotY - p1.plotY) / (p2.plotX - p1.plotX);

        // If slope is negative or zero, line won't reach threshold
        if (slope <= 0) return null;

        // Extrapolate to find crossing point
        const deltaY = targetY - p2.plotY;
        const deltaX = deltaY / slope;
        const crossingX = p2.plotX + deltaX;

        return crossingX;
    }

    // Calculate percentile from a sorted array
    function calculatePercentile(sortedArray, percentile) {
        if (sortedArray.length === 0) return 0;
        if (sortedArray.length === 1) return sortedArray[0];

        const index = percentile * (sortedArray.length - 1);
        const lower = Math.floor(index);
        const upper = Math.ceil(index);
        const weight = index % 1;

        if (lower === upper) {
            return sortedArray[lower];
        }

        return sortedArray[lower] * (1 - weight) + sortedArray[upper] * weight;
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeAnalysis);
    } else {
        initializeAnalysis();
    }
})();
