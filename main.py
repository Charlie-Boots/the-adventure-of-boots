@namespace
class SpriteKind:
    npc = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    mySprite2.say_text("click B to talk", 500, False)
    if controller.B.is_pressed():
        game.show_long_text("hi boots！I'm strong monkey，here is the forest",
            DialogLayout.BOTTOM)
        game.show_long_text("I can let you go but I need to teach you somethings",
            DialogLayout.BOTTOM)
        game.show_long_text("press A to shoot", DialogLayout.BOTTOM)
        tiles.place_on_tile(mySprite2, tiles.get_tile_location(10, 11))
        tiles.set_wall_at(tiles.get_tile_location(9, 12), False)
        tiles.set_wall_at(tiles.get_tile_location(9, 12), False)
    effects.clear_particles(mySprite2)
sprites.on_overlap(SpriteKind.player, SpriteKind.npc, on_on_overlap)

def on_a_pressed():
    pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite2, location):
    global mySprite2
    tiles.set_current_tilemap(tilemap("""
        级别2
        """))
    mySprite2 = sprites.create(img("""
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
            """),
        SpriteKind.npc)
    tiles.place_on_tile(mySprite, tiles.get_tile_location(8, 7))
    tiles.place_on_tile(mySprite2, tiles.get_tile_location(9, 11))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile18
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite3, location2):
    global mySprite3
    sprites.destroy(mySprite2)
    tiles.place_on_tile(mySprite, tiles.get_tile_location(6, 1))
    mySprite.say_text("looks like this is the forest", 2000, False)
    tiles.set_current_tilemap(tilemap("""
        级别3
        """))
    mySprite3 = sprites.create(img("""
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
            """),
        SpriteKind.enemy)
    mySprite3.follow(mySprite, 30)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile20
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite4, location3):
    global mySprite2
    tiles.set_current_tilemap(tilemap("""
        级别0
        """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(9, 14))
    mySprite2 = sprites.create(img("""
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
            """),
        SpriteKind.npc)
    tiles.place_on_tile(mySprite2, tiles.get_tile_location(10, 11))
    sprites.destroy(mySprite3)
scene.on_overlap_tile(SpriteKind.player,
    sprites.castle.tile_grass2,
    on_overlap_tile3)

def on_on_overlap2(sprite5, otherSprite2):
    info.change_life_by(-1)
    pause(2000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

mySprite3: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
tiles.set_current_tilemap(tilemap("""
    级别1
    """))
mySprite = sprites.create(img("""
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
        """),
    SpriteKind.player)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
info.set_life(10)

def on_forever():
    if mySprite.vx > 0:
        mySprite.set_image(img("""
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
            """))
    elif mySprite.vx < 0:
        mySprite.set_image(img("""
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
            """))
forever(on_forever)
