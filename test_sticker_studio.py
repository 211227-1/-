import unittest

from sticker_studio import (
    filter_users_for_admin,
    parse_admin_find_query,
    parse_settitle_payload,
)


class StickerStudioTests(unittest.TestCase):
    def test_parse_settitle_payload_simple(self) -> None:
        short, title = parse_settitle_payload("新标题")
        self.assertIsNone(short)
        self.assertEqual(title, "新标题")

    def test_parse_settitle_payload_with_short(self) -> None:
        short, title = parse_settitle_payload("my_pack | 新标题")
        self.assertEqual(short, "my_pack")
        self.assertEqual(title, "新标题")

    def test_admin_find_filter(self) -> None:
        keyword, filters = parse_admin_find_query("active:true min_clone_done:3 小明")
        self.assertEqual(keyword, "小明")
        self.assertTrue(filters["active"])
        self.assertEqual(filters["min_clone_done"], 3)

        rows = [
            {
                "user_id": 1,
                "username": "alice",
                "display_name": "小明",
                "clone_done_total": 5,
                "make_done_total": 1,
                "invite_count": 0,
                "invited_by": 0,
                "clone_left": 0,
                "make_left": 0,
                "updated_at": "",
                "created_at": "",
            },
            {
                "user_id": 2,
                "username": "bob",
                "display_name": "小红",
                "clone_done_total": 1,
                "make_done_total": 0,
                "invite_count": 0,
                "invited_by": 0,
                "clone_left": 0,
                "make_left": 0,
                "updated_at": "",
                "created_at": "",
            },
        ]
        out = filter_users_for_admin(rows, keyword=keyword, filters=filters, limit=20)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]["user_id"], 1)


if __name__ == "__main__":
    unittest.main()
