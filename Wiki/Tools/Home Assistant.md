---
title: Home Assistant
type: Tool
cover: "[[Wiki/Tools/_covers/home-assistant.png]]"
sources:
related:
  - "[[Docker]]"
  - "[[UTM]]"
  - "[[QEMU]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

Home Assistant is an open-source home automation platform that supports over 2000 integrations for smart devices, sensors, and services. It runs locally, keeping data private, and provides powerful automation capabilities through a YAML-based or visual editor — making it the central nervous system of a connected home.

## Use Cases

- **Smart home control** — Unified interface for lights, switches, climate, media, and security devices across vendors
- **Automation rules** — Trigger actions based on time, state changes, presence, sun position, or complex conditions
- **Energy monitoring** — Track power consumption per device/circuit with the built-in Energy dashboard
- **Presence detection** — Combine phone GPS, network pings, and BLE beacons for reliable occupancy awareness
- **Voice assistant integration** — Local voice control via Wyoming protocol or cloud via Alexa/Google Home

## Examples

### Automation: Turn off lights when everyone leaves

```yaml
automation:
  - alias: "Lights off when away"
    trigger:
      - platform: state
        entity_id: zone.home
        to: "0"
    action:
      - service: light.turn_off
        target:
          entity_id: all
```

### Automation: Morning routine

```yaml
automation:
  - alias: "Morning routine"
    trigger:
      - platform: time
        at: "07:00:00"
    condition:
      - condition: state
        entity_id: binary_sensor.workday_sensor
        state: "on"
    action:
      - service: light.turn_on
        target:
          entity_id: light.bedroom
        data:
          brightness_pct: 30
          color_temp: 400
      - service: media_player.play_media
        target:
          entity_id: media_player.kitchen_speaker
        data:
          media_content_id: "https://radio.example.com/stream"
          media_content_type: "music"
```

### Dashboard card (Lovelace YAML)

```yaml
type: entities
title: Living Room
entities:
  - entity: light.living_room
  - entity: climate.living_room
  - entity: media_player.living_room_tv
  - entity: sensor.living_room_temperature
```

## Links

- **Official site:** https://www.home-assistant.io
- **Repository:** https://github.com/home-assistant/core
- **Documentation:** https://www.home-assistant.io/docs/
