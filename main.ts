namespace SpriteKind {
    export const npc = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.npc, function (sprite, otherSprite) {
    mySprite2.sayText("click B to talk", 500, false)
    if (controller.B.isPressed()) {
        game.showLongText("hi boots！I'm strong monkey，here is the forest", DialogLayout.Bottom)
        game.showLongText("I can let you go but I need to teach you somethings", DialogLayout.Bottom)
        game.showLongText("press A to shoot", DialogLayout.Bottom)
        tiles.placeOnTile(mySprite2, tiles.getTileLocation(10, 11))
        tiles.setWallAt(tiles.getTileLocation(9, 12), false)
        tiles.setWallAt(tiles.getTileLocation(9, 12), false)
    }
    effects.clearParticles(mySprite2)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
	
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile18`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`级别2`)
    mySprite2 = sprites.create(img`
        . . . . f f f f f . . . . . . . 
        . . . f e e e e e f . . . . . . 
        . . f d d d d e e e f . . . . . 
        . f d f d d f d e e f . . . . . 
        . f d f d d f d e e f f . . . . 
        f d e e d d d d e e d d f . . . 
        f d d d d d d d e e b d c . . . 
        f c c c c c d e e e b d c . f f 
        . f d d d d e e e f f c . f e f 
        . f f f f f f e e e e f . f e f 
        . f f f f e e e e e e e f f e f 
        f d d f d d f e f e e e e f f . 
        f d b f d b f e f e e e e f . . 
        f f f f f f f f f f f f e f . . 
        . f e e f e e f . f e e e f . . 
        . f e e f e e f . . f f f f . . 
        `, SpriteKind.npc)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(8, 7))
    tiles.placeOnTile(mySprite2, tiles.getTileLocation(9, 11))
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile20`, function (sprite, location) {
    sprites.destroy(mySprite2)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(6, 1))
    mySprite.sayText("looks like this is the forest", 2000, false)
    tiles.setCurrentTilemap(tilemap`级别3`)
    mySprite3 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . 7 7 7 7 7 7 7 7 . . . . . 
        . . 7 f 7 7 7 7 7 7 f 7 7 . . . 
        . 7 7 f f 7 7 7 7 f f 7 7 7 . . 
        7 7 7 7 f f 7 7 f f 7 7 7 7 . . 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
        7 7 7 7 f 7 7 7 7 f 7 7 7 7 7 . 
        7 7 7 7 f 7 7 7 7 f 7 7 7 7 7 . 
        7 7 7 7 f 7 7 7 7 f 7 7 7 7 7 . 
        7 7 7 7 f 7 7 7 7 f 7 7 7 7 7 . 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
        . 7 7 7 7 7 7 7 7 7 7 7 7 7 . . 
        . 7 7 7 7 7 7 7 7 7 7 7 7 7 . . 
        . . 7 7 7 7 7 7 7 7 7 7 7 . . . 
        `, SpriteKind.Enemy)
    mySprite3.follow(mySprite, 30)
})
scene.onOverlapTile(SpriteKind.Player, sprites.castle.tileGrass2, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`级别0`)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(9, 14))
    mySprite2 = sprites.create(img`
        . . . . f f f f f . . . . . . . 
        . . . f e e e e e f . . . . . . 
        . . f d d d d e e e f . . . . . 
        . f d f d d f d e e f . . . . . 
        . f d f d d f d e e f f . . . . 
        f d e e d d d d e e d d f . . . 
        f d d d d d d d e e b d c . . . 
        f c c c c c d e e e b d c . f f 
        . f d d d d e e e f f c . f e f 
        . f f f f f f e e e e f . f e f 
        . f f f f e e e e e e e f f e f 
        f d d f d d f e f e e e e f f . 
        f d b f d b f e f e e e e f . . 
        f f f f f f f f f f f f e f . . 
        . f e e f e e f . f e e e f . . 
        . f e e f e e f . . f f f f . . 
        `, SpriteKind.npc)
    tiles.placeOnTile(mySprite2, tiles.getTileLocation(10, 11))
    sprites.destroy(mySprite3)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    pause(2000)
})
let mySprite3: Sprite = null
let mySprite2: Sprite = null
let mySprite: Sprite = null
tiles.setCurrentTilemap(tilemap`级别1`)
mySprite = sprites.create(img`
    . . . . f f f f f . . . . . . . 
    . . . f e e e e e f . . . . . . 
    . . f d d d d e e e f . . . . . 
    . c d f d d f d e e f f . . . . 
    . c d f d d f d e e d d f . . . 
    c d e e d d d d e e b d c . . . 
    c d d d d c d d e e b d c . f f 
    c c c c c d d d e e f c . f e f 
    . f d d d d d e e f f . . f e f 
    . . f f f f f e e e e f . f e f 
    . . . . f e e e e e e e f f e f 
    . . . f e f f e f e e e e f f . 
    . . . f e f f e f e e e e f . . 
    . . . f d b f d b f f e f . . . 
    . . . f d d c d d b b d f . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
scene.cameraFollowSprite(mySprite)
info.setLife(10)
forever(function () {
    if (mySprite.vx > 0) {
        mySprite.setImage(img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f e e e e e f . . . 
            . . . . . f e e e d d d d f . . 
            . . . . f f e e d f d d f d c . 
            . . . f d d e e d f d d f d c . 
            . . . c d b e e d d d d e e d c 
            f f . c d b e e d d c d d d d c 
            f e f . c f e e d d d c c c c c 
            f e f . . f f e e d d d d d f . 
            f e f . f e e e e f f f f f . . 
            f e f f e e e e e e e f . . . . 
            . f f e e e e f e f f e f . . . 
            . . f e e e e f e f f e f . . . 
            . . . f e f f b d f b d f . . . 
            . . . f d b b d d c d d f . . . 
            . . . f f f f f f f f f . . . . 
            `)
    } else if (mySprite.vx < 0) {
        mySprite.setImage(img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d d d e e e f . . . . . 
            . c d f d d f d e e f f . . . . 
            . c d f d d f d e e d d f . . . 
            c d e e d d d d e e b d c . . . 
            c d d d d c d d e e b d c . f f 
            c c c c c d d d e e f c . f e f 
            . f d d d d d e e f f . . f e f 
            . . f f f f f e e e e f . f e f 
            . . . . f e e e e e e e f f e f 
            . . . f e f f e f e e e e f f . 
            . . . f e f f e f e e e e f . . 
            . . . f d b f d b f f e f . . . 
            . . . f d d c d d b b d f . . . 
            . . . . f f f f f f f f f . . . 
            `)
    }
})
