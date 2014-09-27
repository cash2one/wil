#!/usr/bin/env coffee
config =


main:
    res: 1
    x: 0
    y: 349

equipButton:
    res: 8
    dummyRes: true
    resOnClick: 8
    x: 643
    y: 61
    father: "main"
    commands:
        status:
            switchBoolean: "visible"
            page: "equipments"

bagButton:
    res: 9
    dummyRes: true
    resOnClick: 9
    x: 682
    y: 41
    father: "main"
    commands:
        bag:
            switchBoolean: "visible"

skillButton:
    res: 10
    dummyRes: true
    resOnClick: 10
    x: 722
    y: 21
    father: "main"
    commands:
        status:
            switchBoolean: "visible"
            page: "skills"

soundButton:
    res: 11
    dummyRes: true
    resOnClick: 11
    x: 764
    y: 11
    father: "main"


bag:
    res: 3
    x: 20
    y: 20
    hidden: true
    draggable: true
    hotkeys:
        65:
            switchBoolean: "visible"

bagClose:
    res: 371
    dummyRes: true
    resOnClick: 371
    x: 309
    y: 203
    father: "bag"
    commands:
        bag:
            visible: false

gold:
    res: 27
    dummyRes: true
    x: 10
    y: 190
    father: "bag"
    page: "gold1"
    pages: ["gold1", "gold2", "gold3"]
    commands:  # test switch gold
        gold:
            pageSwitch: +1

gold1:
    res: 27
gold2:
    res: 28
gold3:
    res: 29


status:
    res: 370
    x: 565
    y: 10
    hidden: true
    draggable: true
    page: "points"
    pages: ["equipments", "points", "miscellaneous", "skills"]
    hotkeys:
        81:
            switchBoolean: "visible"
            page: "equipments"
        87:
            switchBoolean: "visible"
            page: "skills"
        69:
            switchBoolean: "visible"

statusClose:
    res: 371
    dummyRes: true
    resOnClick: 371
    x: 8
    y: 39
    father: "status"
    commands:
        status:
            visible: false

statusPageUp:
    res: 373
    dummyRes: true
    resOnClick: 373
    x: 7
    y: 128
    father: "status"
    commands:
        status:
            pageSwitch: -1

statusPageDown:
    res: 372
    dummyRes: true
    resOnClick: 372
    x: 7
    y: 187
    father: "status"
    commands:
        status:
            pageSwitch: +1


points:
    res: 382
    dummyRes: true  # show original status
    x: 38
    y: 52


miscellaneous:
    res: 382
    x: 38
    y: 52


skills:
    res: 383
    x: 38
    y: 52

skillsPageUp:
    res: 398
    resOnClick: 399
    x: 175
    y: 62
    father: "skills"
    commands: "command1"  # test

skillsPageDown:
    res: 396
    resOnClick: 397
    x: 175
    y: 92
    father: "skills"


equipments:
    res: 376
    dummyRes: true
    x: 38
    y: 52
    page: "equipmentsM"
    pages: ["equipmentsM", "equipmentsW"]
    commands:
        equipments:
            pageSwitch: +1

equipmentsM:
    res: 376
equipmentsW:
    res: 377



console.log(JSON.stringify(config))  # usage: ./ui.coffee >ui.json
# END
