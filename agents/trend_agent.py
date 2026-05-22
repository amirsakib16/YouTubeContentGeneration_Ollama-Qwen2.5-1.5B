from tools.youtube_trends import YouTubeTrendTool
class TrendResearchAgent:
    def __init__(self, youtube_api_key):
        self.youtube = YouTubeTrendTool(youtube_api_key)
    def run(self):
        trends = self.youtube.get_trending_videos()
        return {"trending_topics": trends}