#!/usr/bin/env coffee
config =

debugText:
    text:
        src: "{0} {1} {2} {3}"
        model: "hp mp exp weight"

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
    mouse:
        click:
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
    mouse:
        click:
            bag:
                switchBoolean: "visible"

skillButton:
    res: 10
    dummyRes: true
    resOnClick: 10
    x: 722
    y: 21
    father: "main"
    mouse:
        click:
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
    mouse:
        click:
            bag:
                visible: false

bagUse:
    res: 26
    dummyRes: true
    resOnClick: 26
    x: 254
    y: 183
    father: "bag"

bagGold:
    res: 27
    dummyRes: true
    x: 10
    y: 190
    father: "bag"
    page: "gold1"
    pages: ["gold1", "gold2", "gold3"]
    mouse:
        click:  # test switch gold
            bagGold:
                pageDelta: +1

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
    mouse:
        click:
            status:
                visible: false

statusPageUp:
    res: 373
    dummyRes: true
    resOnClick: 373
    x: 7
    y: 128
    father: "status"
    mouse:
        click:
            status:
                pageDelta: -1

statusPageDown:
    res: 372
    dummyRes: true
    resOnClick: 372
    x: 7
    y: 187
    father: "status"
    mouse:
        click:
            status:
                pageDelta: +1


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
    mouse:
        rightClick: "test"

skillsPageUp:
    res: 398
    resOnClick: 399
    x: 175
    y: 62
    father: "skills"
    mouse:
        click: "test"

skillsPageDown:
    res: 396
    resOnClick: 397
    x: 175
    y: 92
    father: "skills"
    mouse:
        doubleClick: "test"
        rightClick: "test"


equipments:
    res: 376
    dummyRes: true
    x: 38
    y: 52
    page: "equipmentsM"
    pages: ["equipmentsM", "equipmentsW"]
    mouse:
        click:
            equipments:
                pageDelta: +1

equipmentsM:
    res: 376
equipmentsW:
    res: 377


hpmp:
    x: 38
    y: 90
    father: "main"
    page: "hpmpBallEmpty"
    pages: ["hpBallEmpty", "hpmpBallEmpty"]
    mouse:
        click:
            hpmp:
                pageDelta: +1

hpBallEmpty:
    res: 5

hpBallHpFull:
    res: 6
    father: "hpBallEmpty"
    model: "hp maxhp /"
    view: "viewY"

hpmpBallEmpty:
    res: 4
    dummyRes: true
    x: 2
    y: 1

hpmpBallHpFull:
    res: 4
    resRect: [0, 0, 0.5, 1]
    father: "hpmpBallEmpty"
    model: "hp maxhp /"
    view: "viewY"

hpmpBallMpFull:
    res: 4
    resRect: [0.5, 0, 0.5, 1]
    father: "hpmpBallEmpty"
    model: "mp maxmp /"
    view: "viewY"


lv:
    res: 30
    x: 665
    y: 147
    father: "main"


exp:
    res: 7
    x: 665
    y: 178
    father: "main"
    model: "exp maxexp /"
    view: "viewW"
    mouse:
        mouseOver:
            expText:
                visible: true
        mouseOut:
            expText:
                visible: false

expText:
    father: "exp"
    hidden: true
    text:
        src: "{0}  {1}"
        model: "exp maxexp / weight"
        formatter: "currency"
        font: "font1"


weight:
    res: 7
    x: 665
    y: 210
    father: "main"
    model: "weight maxweight /"
    view: "viewW"



print = console.log.bind(console)
print(JSON.stringify(config))  # usage: ./ui.coffee >ui.json
# END
