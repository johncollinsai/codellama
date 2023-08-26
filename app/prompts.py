# gpt-4
INTRO_SENTENCE = """
{modality} provides the following information for {prompt} for these topics:
• General
• Corporate
• Compliance
• Relationships between {prompt} and its subsidiaries and directors
• Indications of financial distress
• Involvement in litigation and disputes
• {prompt}'s profile and media coverage

Detailed responses by topic:
"""

USER_PROMPT = """
You are an AI trained by OpenAI, specialized in conducting due diligence for companies. Your task is to provide a comprehensive due diligence report about {prompt} which includes the following sections:

1. General: List 4 key findings from recent investigations.
2. Corporate: List 4 critical corporate facts.
3. Compliance: Describe regulatory notices, sanction, embargo, and financial enforcements against {prompt} and its subsidiaries or directors citing 4 recent cases.
4. Relationships: Describe 4 important relationships between {prompt} and its subsidiaries or directors or associated off-shore companies.
5. Financial Distress Indicators:
    - Assets & Liabilities: List 4 recent and critical facts.
    - Cashflows & Liquidity: List 4 recent and critical key metrics.
    - Key Financial Ratios: List 4 recent and critical financial ratios.
6. Litigation & Disputes: Describe litigation or bankruptcy proceedings against {prompt} and its subsidiaries or directors citing 4 recent cases.
7. Profile and media: Summarize 4 recent high profile media or social media commentaries.

Use the bullet point format • to structure your findings in each section and start with this sentence: '{intro_sentence}'.
"""

# llama-2-7b
USER_PROMPT_LLAMA = """
Can you provide detailed and accurate information necessary for a due diligence report about {prompt}?
"""

# USER_PROMPT_LLAMA = """
# Please provide a due diligence report for the company {prompt}. This should include:
# - Key facts and findings about the company's corporate structure and business operations.
# - Information about the company's compliance history, including any recent regulatory notices, sanctions, embargoes, or financial enforcements.
# - A description of significant relationships between the company and its subsidiaries, directors, or associated offshore companies.
# - An overview of any indicators of financial distress, including details about the company's assets, liabilities, cash flows, liquidity, and key financial ratios.
# - A summary of the company's involvement in litigation and disputes.
# - Information about the company's reputation and any significant recent media coverage.
# """

