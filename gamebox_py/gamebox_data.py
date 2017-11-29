import framebuf

sprite_games_data = bytearray(b'\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\xff\x7f\x00\x80\x00\x80\x00@\x00\x00\x01@\x02l\x01@\xb7m\x01@\x02\x00\x01@\xf0\x07\x01\x80\x0f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00pL\xf4\x1e\x88\xd2\x16\x02\x08R\x15\x02\x08R\xf4\x1e\xc8^\x14\x10\x88R\x14\x10\xf0R\xf4\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

sprite_config_data = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x01\x00\x00\x98\x19\x00\x00\xf8\x1f\x00\x00p\x0e\x00\x000\x0c\x00\x00\x1c8\x00\x00\x1c8\x00\x000\x0c\x00\x00p\x0e\x00\x00\xf8\x1f\x00\x00\x98\x19\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\'z9\xa2(\nE\x82h\n\x05\x82\xa8z\x05\x82(\x0be\xa2(\nE\x1c\'\ny\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

sprite_games = framebuf.FrameBuffer(sprite_games_data, 32, 32, framebuf.MONO_HMSB)

sprite_config = framebuf.FrameBuffer(sprite_config_data, 32, 32, framebuf.MONO_HMSB)