## LLM Evaluations with PromptFoo

Test-drive your prompts and models with automated, reliable evaluations.

[![🚀 Test Driven Prompt Engineering with PromptFoo (12 min)](https://i.ytimg.com/vi_webp/KhINc5XwhKs/sddefault.webp)](https://youtu.be/KhINc5XwhKs
<youtube_summary>This video discusses how to create effective, repeatable prompts for applications by using a structured prompt evaluation and testing framework called Prompt Fu. The challenge in prompt engineering is the lack of a framework to measure and compare prompts or LLM providers, which makes it hard to know if changes improve or worsen results. Prompt Fu helps developers produce cheaper, faster, and more accurate prompts by enabling test-driven prompt engineering.

The presenter demonstrates using Prompt Fu with VS Code, showing how to set up and run tests easily. Prompt Fu uses a simple configuration involving three core components: providers (LLMs), prompts, and test cases with variables and assertions. Variables dynamically change inputs to prompts, while assertions validate outputs against expected criteria, such as checking if the response contains certain keywords or matches patterns. Prompt Fu supports diverse assertion types, including regex, custom code, Levenshtein distance, and an LLM rubric that uses LLMs to evaluate prompt outputs (e.g., verifying sentiment or query type).

An example compares OpenAI’s GPT-4 Turbo and GPT-3.5 Turbo models on a natural language query prompt for SQL. Results show GPT-3.5 Turbo delivers the needed output much faster and at a quarter of the token cost compared to GPT-4, which returns additional unneeded information. This insight allows developers to optimize for cost and speed without sacrificing accuracy.

The testing framework runs each prompt multiple times with different inputs and providers, producing detailed reports and a web-based viewer for easier analysis. Cached results can be disabled to get fresh outputs each run. The video stresses the importance of centralized prompt storage and automated testing to prevent regressions, save time, reduce costs, and build confidence before deploying prompts in production applications.

Prompt Fu supports multiple LLM providers and is extensible, with documentation and examples available in the linked GitHub repo. The presenter encourages adopting test-driven prompt development—writing tests first and then creating prompts to pass them—to improve prompt quality and reliability. Overall, Prompt Fu is recommended as a simple, customizable tool that helps engineers and product builders optimize prompts in the evolving AI landscape, enabling faster shipping of better, cost-effective AI-powered tools and applications.</youtube_summary>
)

PromptFoo is a test-driven development framework for LLMs:

- **Developer-first**: Fast CLI with live reload & caching ([promptfoo.dev](https://promptfoo.dev))
- **Multi-provider**: Works with OpenAI, Anthropic, HuggingFace, Ollama & more ([GitHub](https://github.com/promptfoo/promptfoo))
- **Assertions**: Built‑in (`contains`, `equals`) & model‑graded (`llm-rubric`) ([docs](https://www.promptfoo.dev/docs/configuration/expected-outputs/))
- **CI/CD**: Integrate evals into pipelines for regression safety ([CI/CD guide](https://www.promptfoo.dev/docs/integrations/ci-cd/))

To run PromptFoo:

1. Install Node.js & npm ([nodejs.org](https://nodejs.org/))
2. Set up your [`OPENAI_API_KEY`](https://platform.openai.com/api-keys) environment variable
3. Configure `promptfooconfig.yaml`. Below is an example:

```yaml
prompts:
  - |
    Summarize this text: "{{text}}"
  - |
    Please write a concise summary of: "{{text}}"

providers:
  - openai:gpt-3.5-turbo
  - openai:gpt-4

tests:
  - name: summary_test
    vars:
      text: "PromptFoo is an open-source CLI and library for evaluating and testing LLMs with assertions, caching, and matrices."
    assertions:
      - contains-all:
          values:
            - "open-source"
            - "LLMs"
      - llm-rubric:
          instruction: |
            Score the summary from 1 to 5 for:
            - relevance: captures the main info?
            - clarity: wording is clear and concise?
          schema:
            type: object
            properties:
              relevance:
                type: number
                minimum: 1
                maximum: 5
              clarity:
                type: number
                minimum: 1
                maximum: 5
            required: [relevance, clarity]
            additionalProperties: false

commandLineOptions:
  cache: true
```

Now, you can run the evaluations and see the results.

```bash
# Execute all tests
npx -y promptfoo eval -c promptfooconfig.yaml

# List past evaluations
npx -y promptfoo list evals

# Launch interactive results viewer on port 8080
npx -y promptfoo view -p 8080
```

PromptFoo caches API responses by default (TTL 14 days). You can disable it with `--no-cache` or clear it.

```bash
# Disable cache for this run
echo y | promptfoo eval --no-cache -c promptfooconfig.yaml

# Clear all cache
echo y | promptfoo cache clear
```
