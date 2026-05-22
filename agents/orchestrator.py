from agents.trend_agent import TrendResearchAgent
from agents.strategist_agent import StrategistAgent
from agents.script_agent import ScriptAgent
from agents.seo_agent import SEOAgent

class ContentOrchestrator:
    def __init__(self, youtube_api_key):
        self.trend_agent = TrendResearchAgent(youtube_api_key)
        self.strategy_agent = StrategistAgent()
        self.script_agent = ScriptAgent()
        self.seo_agent = SEOAgent()
    def run(self):
        trends = self.trend_agent.run()
        strategy = self.strategy_agent.run(trends["trending_topics"])
        scripts = self.script_agent.run(strategy)
        seo = self.seo_agent.run(strategy)

        return {"trends": trends, "strategy": strategy, "scripts": scripts, "seo": seo}