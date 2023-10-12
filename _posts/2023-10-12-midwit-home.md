---
layout: post
title: The midwit home
image: /img/midwit-home/home.jpg
tags: 
description: "Less automation and less agony"
excerpt: ""
permalink: /midwit-home/
background_color: rgb(215,216,218)
category: "self improvement"
head: "<style>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-top: 2.3em;
  margin-bottom: -0.5em;
  max-width: calc(max(50%,300px));
  max-height: 9em;
}
</style>
"
comment:
  substack: https://dynomight.substack.com/p/midwit-home
---

Reading a book one night, you decide to turn on the lights. And suddenly it's obvious. Hauling your body across the room just to flip a switch is absurd. So you decide to get smart lights. Two hours later, your world is pain:

- Z-Wave
- Zigbee
- MQTT
- Matter
- Thread
- Echo
- Google Home
- Apple Home
- HomeKit
- Homebridge
- Home Assistant
- Hue
- deCONZ
- Sharp tools
- IFTTT
- Tuya
- Nest
- RBOY
- TRÅDFRI
- Hubitat
- SmartThings
- WiFi repeaters
- Mesh networks
- Powerline networks
- WiFi AX
- WiFi 2.4 GHz
- WiFi 5 GHz
- WiFi 6
- high gain antennas
- Integrations
- MQTT
- ESPHome
- KNX

The hell? But people seem to think that Home Assistant is good. (Something about subscription fees and invasive apps and forced obsolescence?) So you search for "how to get a Home Assistant". This reveals a recursive landscape of terror:

- Home Assistant Operating System
- Home Assistant Container
- Home Assistant Supervised
- Home Assistant Core
- Home Assistant OS
- Home Assistant Yellow
- Home Assistant Green
- curl
- tarball
- sudo
- ssh
- NUC
- Rasberry Pi
- Blueprints
- NAS
- VirtualBox
- Docker
- Ubuntu
- Debian
- Python
- pip3
- Virtual environments
- Proxmox
- Hypervisor
- LXC
- M.2 slots
- YAML
- SQLite
- Wireguard
- SkyConnect
- Z-WaveJS2MQTT

In desperation you go to a smart home forum and make a post titled "smart lights no agony please help dear god". The first response is:

> Just get a Qetzl hub, a OTOROXv3.2 bridge, and any MongoChopper compatible bulbs. After matroid paring, you can connect `xmpf12` beacons and trigger them with plain-old SkyDust switches. Are you *trying* to make this complicated?

Which sounds lovely. But then there's many replies like this:

> MongoChopper only works in reticulated mode, which newer Qetzl hubs don't support. Easier to just make a custom Hellfire demarkation loop.

(Just. Always "just".)

Eventually you admit you've already suffered more than a lifetime of flipping switches and go to bed, mournful of your four lost hours of reading. You dream of a giant planetary light switch, glowing in brutal simplicity.

---

So. Many people feel this way. Dumb homes are fine, but require flipping switches. Smart homes *should* be better, but in practice the cost of administering a new home IT nightmare outweighs the benefits. 

But perhaps there's a third way. What if you try to achieve the goals of a smart home, but you rule out anything that involves getting two computers to talk to each other? So apps, phones, and hubs are out. But doorbells are good. Garage door openers are good. Dishwashers and smoke alarms are great. What else is there like that?

Quite a lot, arguably.

## Things that exist

I have "no club that would have me" relationship with links for things you can buy: They're convenient, but it's [hard to be sure](/ikea-purifier/) of the motivations of anyone who provides them. So no links here, affiliate or otherwise. They wouldn't be very useful anyway since most of this stuff is sold by brands like ELFPUFF that disappear after two weeks.

<img class="center" src="/img/midwit-home/remote-outlet.jpg" alt="remote controlled outlet">

**Remote-controlled outlets.** These are probably the easiest win for most people. Plug stuff into the cubes, plug the cubes into the wall, and use the remote to control which cubes are active. The buttons work *instantly*, with a range of 30 m (100 ft) even through walls. There is no app or WiFi. One button can control multiple plugs and the same plug can be paired to multiple remotes. (Cost: Around $25 for five plugs and two remotes.)

The obvious use for these is lights. When your roommate complains about you strobing them (it's irresistible) remind them that LED bulbs' lifespans are not shortened by on/off cycles. They're also great for fans, air purifiers, and humidifiers.

Or, you can use this as a remote for a dumb window-unit air conditioner. (Make sure to check the rated current.)

Or, you can use this as a *signal*—put a light in the basement for grandma to activate if she needs you. Or put lights in rooms around the house all paired to one button, and strobe them when you want everyone to gather for dinner.

Or, you can use this for tea. My usual process for making tea is to walk to the kitchen and start the kettle. Then, because it takes an eternity for water to boil, I go back to my desk to wait. Then I forget about the tea. With this remote you can leave the kettle in a "ready" state: filled with water, kettle on, outlet off. Activate the remote a few minutes ahead of time and make tea in a single trip with no waiting.

Or, my printer is cursed. After being on for a few days it refuses to print anything longer than two pages. I know this shouldn't be possible, but I've exhausted every avenue for fixing it. I could get a new printer, but maybe it's a network issue or something?

Restarting the printer fixes it. But the printer has one of those infuriating power buttons where you hold it for ten seconds and then it ignores you. So for a year, I'd walk to the room with the printer and reach deep inside the cabinet to physically unplug and re-plug it. Now I use one of these cubes and remotely power cycle it when necessary. Utterly graceless, but effective.

<img class="center" src="/img/midwit-home/remote-socket.jpg" alt="remote controlled light socket">

**Remote-controlled light sockets**. These are the same as the above, except they work on light sockets rather than outlets. Less versatile, but work with built-in light fixtures. ($30 for 5 sockets and 2 remotes)

<img class="center" src="/img/midwit-home/remote-bulb.jpg" alt="remote controlled light bulb">

**Remote-controlled light bulbs.** Personally, I'd never buy these, because I'm fanatical about color quality. (It's futile to start with low-quality photons and then try to arrange matter to make them look good.) And if you have multiple bulbs and one remote, what do you do when one bulb breaks?

But they do exist. The remote talks directly to the light bulbs with no WiFi. And if you want dimming or changing colors, this seems to be the only midwit option. ($20 for 4 bulbs and 2 remotes)

<img class="center" src="/img/midwit-home/motion-bulb.jpg" alt="motion bulb">

**Motion sensing light bulbs**. These have a small sensor at the tip. Put them into any light figure and then leave it on. After sensing motion, the bulb actives for a while. Great for dark stairs. ($5-10 per bulb)

<img class="center" src="/img/midwit-home/motion-bulb-socket.jpg" alt="motion bulb socket">

**Motion sensing bulb sockets**. These turn any bulb into a motion-sensing bulb. In principle, it seems good to separate the motion sensing bits from the glowy bits. But in practice the front assembly blocks the sensor from seeing straight ahead, so it may not be the way to go. It also looks very, uhh, long. ($11)

<img class="center" src="/img/midwit-home/motion-outlet.jpg" alt="motion controlled outlet">

**Motion sensing outlets**. When these sense motion, they activate the plug for a configurable amount of time. ($20 per plug)

One application is to *sense* motion in a different place from where you want light. But there are many other uses. Some people with kids put these on window unit air conditioners in rarely used rooms, so they aren't constantly nagging them to turn things off.

Or, despite cats' contempt for human life, many people keep them as pets. When cats use litter boxes, they produce undesirable smells. You can connect an air purifier to one of these to automatically turn on and remove those smells.

<img class="center" src="/img/midwit-home/remote-motion-outlet.jpg" alt="remote motion controlled outlet">

**Remote motion sensing outlets**. For even more flexibility, these use battery-operated motion sensors, which can be far away from the outlet. ($26)

Not totally sure where these would be useful. Maybe if you have a bunch of roommates and one bathroom, you could put the sensor in the bathroom and a light in a public room, so people would know when the bathroom is free? Seems weird.

<img class="center" src="/img/midwit-home/battery-motion-lights.jpg" alt="battery powered motion-sensing lights">

**Battery-powered motion sensing lights.** These are small battery-powered lights that activate when they sense motion. Every time you open your closet and the light goes on, it feels like a little message from the universe that you matter. ($3-10 each.)

<img class="center" src="/img/midwit-home/clapper.jpg" alt="The Clapper" style="max-height:20em;">

**The Clapper**. When this outlet hears sounds at the right frequency separated by the right interval, it switches on or off. It was first sold in 1984 and as far as I can tell hasn't been significantly updated since except to add a Bob Ross module. (Yes, this really exists. It gives quotes when you clap three times.) ($20)

I'm confused. The Clapper seems to work fine. Why isn't it more popular? I *think* it's partly that it was originally marketed as an aid to the infirm and elderly rather than Retro Home Automation for Your Active Lifestyle. But why aren't there new variants?  The [patent](https://patents.google.com/patent/US5493618) is long expired, but there seem to be few (and bad) competitors. There are even rumors that quality has declined for brand-name Clappers.

<img class="center" src="/img/midwit-home/fyrtur.jpg" alt="motorized blinds">

**Motorized shades/blinds with physical remotes**. If you look at reviews for IKEA's shades or blinds, there are many complaints about trying to pair them with a hub and phone. But you don't need a hub! They come with a physical remote and there's physical process to control how far they drop. Though sadly you lose the ability to set daily schedule or program them to move randomly and scare your dog. ($130-infinity)

<img class="center" src="/img/midwit-home/24-hour-timer.jpg" alt="mechanical outlet timer">

**Mechanical outlet timers**: You plug this into an outlet, it slowly spins once per day, and the pins determine is the outlet is active for each 30 minute period. ($5-10)

This! This is the kind of thing I need more of in my life! I *really* think it deserves to be more celebrated as a triumph of design. But it's existed for decades and I can't find the original inventor.

Many use these with light for plants. Or, it can be nice to wake up with light rather than sound. Instead of buying a light alarm clock, you can just plug a lamp into one of these. Or, if you buy into the rationalist trend of *very bright* lights, then you can rig up one of these up and have each day greet you with 100k lumens gently screaming into your face.

Or, in winter, I use a ([non-ultrasonic](/humidifiers/!) humidifier. But it's only really useful for a couple of hours before going to bed, after which humans provide plenty of humidity. Using a timer automates things, saves energy, and avoids humidity getting out of control in the middle of the night. Even better, it reduces how often you need to refill the tank.

<img class="center" src="/img/midwit-home/24-hour-timer-digital.jpg" alt="digital outlet timer">

**Digital outlet timers**: A good alternative if you need more precise timing or find mechanical timers too beautiful and intuitive and bulletproof. ($15)

<img class="center" src="/img/midwit-home/countdown-timer.jpg" alt="countdown timer">

**Countdown outlet timer**. Press a button and activate an outlet for a given period of time. Good for lights, air purifiers, heaters, and the paranoid. ($10-20)

<img class="center" src="/img/midwit-home/door-alarm.jpg" alt="door alarm">

**Door alarm / reminder.** You mount a magnet on one side of a door and the detector on the other. You can configure it to either make noise immediately when opened or after a certain amount of time. Useful for doors or windows or refrigerator doors that are sometimes left open. ($4-20 per alarm, depending on how many you buy.)

<img class="center" src="/img/midwit-home/door-fob.jpg" alt="door fob">

**Key fobs for home doors**. Unlock your home like you unlock a car. There's even a battery-powered version that sticks on top of the inside lock and opens the door by physically turning the existing latch. And apparently this sort of works? This makes me nervous, though I know physical locks aren't very secure anyway. ($50+)

<img class="center" src="/img/midwit-home/blumat2.jpg" alt="watering stakes">

**Watering stakes**. The one true home decoration strategy is: plants. If you don't have any plants, forget home intelligence levels and get some plants. Now, to keep them alive, you put one of these stakes in the soil and the end of the cable in a container of water. The soil then stays damp through voodoo magic. (It's not a siphon because the water can be below the plant.) Purely physical, no electronics. In principle, this can work for a *very* long time if you have a big enough container of water. You can also make a crappy DIY version by drilling a tiny hole in the lid of a plastic bottle. ($5 / stake.)

<img class="center" src="/img/midwit-home/water-detector.jpg" alt="water detector">

**Water detector**. This flashes and screams if water contacts the base. Batteries last for years. ($7-10 each)

<img class="center" src="/img/midwit-home/robot.jpg" alt="vacuum robot">

**Robot vacuums with a physical remote**. These still exist, for now! You can set a daily schedule without giving ~~iRobot~~ Amazon a map of your home.

<img class="center" src="/img/midwit-home/temp-outlet.jpg" alt="temperature controlled outlet">

**Temperature controlled outlets**. Plug a device into it and plug it into the wall. The plug turns on and off when programmable temperatures are reached. ($20-30)

Did the temperature sensor in your fridge break, meaning it stays on all the time? Does the manufacturer demand your first child for a new sensor? Plug the fridge into one of these.

<img class="center" src="/img/midwit-home/charger.jpg" alt="rechargable batteries">

**Rechargeable batteries.** You already knew these existed. But did you know how much better they've gotten in recent years? I bring this up because where possible I advise avoiding things with built-in batteries. Partly that's so the lifespan isn't limited by the battery. But it's also more convenient: To recharge, you swap the batteries with the ones on the charger and you're done. This is much easier than going through a remove / find charger / charge / wait / replace cycle.


## Lessons

One lesson is that **lights do well**. Half of smart homes seem to be about lights. By combining remotes, motion sensors, timers, and maybe Clappers, you can go quite far with lights just using midwit solutions.

A second is that **power is the interface**. All of the above items are either single devices, or devices that "communicate" with each other by the brute force method of turning power on or off for each other. It's interesting how far that takes you.

Finally, **dumber devices are often more interoperable**. Physical on/off switches are good. If a device has one, then you can set it to "on" and then control it through an external remote or whatever. But increasingly many things have clever touch sensor power buttons. These can't be activated without pressing the button, so none of this works.

(BTW, manufacturers, if you want to use touch sensors and you don't want to lose the *massive* midwit market, make things that automatically turn on when first connected to power, without waiting for a touch.)

## Things I wish existed

There are many things that would make midwit life better, and it seems like *could* be made, but aren't.

1. **Remote controlled dimmers.** Modern dimmers work by truncating the lower-amplitude parts of the alternating current—basically switching the lights on and off very quickly. There should be light-bulb sockets with a remote to control the dimming level.
  
2. **Whistle controlled power switches.** Clapping is (mildly) annoying. Couldn't we use other sounds?
  
3. **PM<sub>2.5</sub> controlled outlets.** The biggest advantage of commercial air purifiers over DIY versions is that some integrate air quality sensors and turn on automatically when needed. I want a device that samples the air and activates an outlet if PM<sub>2.5</sub> is above a threshold.

4. **Remote-controlled wall-switch pressers.** This is rather cursed, but I'd like a device to physically flip my existing wall switches when activated by a remote, so my lights can be be dumb *and* midwit. (There are "smart" variants now, but seemingly no midwit versions.)

5. **Power-controlled remote pressers.** This is *utterly* cursed, but hear me out: I want a gadget that I physically attach to a remote. When the gadget gets power, it presses the "on" button on the remote. When it loses power, it presses the "off" button.
   
   Why? Because then you could automate anything with a remote! If I have remote-controlled motorized blinds, I'd like to put the remote into this gadget, and then plug the gadget into an an outlet timer for a daily schedule. Or use a Clapper or motion sensor or whatever.

   Like I said, cursed. Maybe it could just memorize and repeat the signal from remote instead of physically pressing buttons?

6. **Remote-controlled light sockets that respond to power cycles.** The annoying thing about remote-controlled light sockets is they render your existing switches useless. There is no need! I want a variant that works like this: If the power is quickly turned off and on again, the outlet switches from powered to unpowered (or vice-versa). Then you could use remotes *and* existing switches, with the only downside that you need to remember to "double flip" all your lights.

7. **Gates.** Say you have Clapper-activated lights in your bedroom, but you do a lot of sleep-clapping. Well, you can plug the lights into a Clapper, and the Clapper into an outlet timer. That's basically an AND gate.

   But what about OR gates? What if you want to turn on an air conditioner when there is motion *or* if the temperature goes above X degrees? I think an OR gate would just amount to a "splitter", except with multiple inputs and one output. But this doesn't seem to be something you can buy, perhaps because if the inputs came from different circuits that would cause explosions?

   Or how about NOT gates? Maybe you have an air purifier that's really loud, so you only want it to run when you're not in the room. There should be a gadget that reverses the power signal provided by a motion sensor.

   But then, how would a NOT gate work? The gadget would need to plug into the wall to provide power when the signal is off. Which means that *really* it would be a (NOT SIGNAL) AND (MAINS) gate. Or maybe could be an XOR gate instead?

   Or can we hand NAND gates? Or NOR gates? There's no obvious need, true. But I'd rest easier knowing my janky kettle control system was built out of functionally complete base units.