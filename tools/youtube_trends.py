from googleapiclient.discovery import build
class YouTubeTrendTool:
    def __init__(self, api_key):
        self.youtube = build("youtube", "v3", developerKey=api_key)
    def get_trending_videos(self):
        request = self.youtube.videos().list(
            part="snippet,statistics",
            chart="mostPopular",
            regionCode="US",
            maxResults=10)
        response = request.execute()
        trends = []
        for item in response["items"]:
            trends.append(item["snippet"]["title"])

        return trends