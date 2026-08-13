# https://github.com/manoharchalla-inor
# #manoharchalla-in
import unittest
import sys
from pathlib import Path

# Add src/ to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils.config import Config
from agents.content_agent import ContentAgent

class TestGenMitraPipeline(unittest.TestCase):
    def test_01_config_initialization(self):
        self.assertIsNotNone(Config.BRAND_NAME)
        self.assertIsInstance(Config.POST_TIMES, list)
        self.assertEqual(len(Config.POST_TIMES), 5)

    def test_02_fallback_copywriting(self):
        agent = ContentAgent()
        topic = {
            "title": "AI in Enterprise Automation",
            "summary": "AI is transforming enterprise workflows.",
            "source": "TechCrunch",
            "viral_angle": "How AI saves 10 hours a week.",
            "hook_idea": "Stop wasting time on manual data entry."
        }
        post = agent._fallback(topic, slot=0)
        self.assertIn("hook", post)
        self.assertIn("body", post)
        self.assertIn("hashtags", post)
        self.assertTrue(post["status"] in ["draft", "ready"])

    def test_03_preview_publishing(self):
        agent = ContentAgent()
        topic = {
            "title": "Future of Remote Work",
            "summary": "Remote work trends in 2026.",
            "source": "HBR",
            "viral_angle": "Why hybrid models succeed.",
            "hook_idea": "The office as we knew it is gone."
        }
        post = agent._fallback(topic, slot=1)
        self.assertIsNotNone(post.get("hook"))
        self.assertTrue(len(post.get("hashtags", "")) > 0)

if __name__ == "__main__":
    unittest.main()
