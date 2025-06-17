## LLM Agents: Building AI Systems That Can Think and Act

LLM Agents are AI systems that can define and execute their own workflows to accomplish tasks. Unlike simple prompt-response patterns, agents make multiple LLM calls, use tools, and adapt their approach based on intermediate results. They represent a significant step toward more autonomous AI systems.

[![Building LLM Agents with LangChain (13 min)](https://i.ytimg.com/vi_webp/DWUdGhRrv2c/sddefault.webp)](https://youtu.be/DWUdGhRrv2c
<youtube_summary>The speaker discusses the concept of agents in LangChain, focusing on their use as reasoning engines that dynamically decide actions based on user input and previous results, rather than following fixed sequences. Agents enable integration with external tools like search APIs and databases, overcoming language model limitations such as lack of real-time data and poor math skills. Benefits include flexibility, error recovery, and handling multi-step tasks, exemplified by querying SQL databases.

A typical agent workflow involves receiving a user query, the language model selecting and interacting with tools, observing outputs, and iterating until a stopping condition is met, often when the model decides the task is complete. The main prompting strategy is ReAct (Reasoning and Acting), which combines chain-of-thought reasoning with tool usage to improve accuracy and reliability, demonstrated through multi-hop question answering on datasets like HotpotQA.

Challenges in agent development include:  
1. Ensuring appropriate tool usage by providing clear tool descriptions and employing retrieval methods to handle many tools without exceeding prompt length limits. Few-shot examples and fine-tuning (e.g., Toolformer) also aid tool selection.  
2. Avoiding unnecessary tool use during conversational interactions by instructing the model or adding a “return to user” tool to encourage direct responses.  
3. Parsing language model outputs (which command tool usage) reliably into executable actions, often using structured formats like JSON and modular output parsers that can retry or correct errors.  
4. Maintaining memory of previous steps and interactions to handle long-running tasks without exceeding context windows, using retrieval of recent and relevant actions and observations. Handling large API responses may involve summarization or selective key extraction.  
5. Keeping agents on track by reiterating objectives frequently in prompts and separating planning from execution steps, as seen in Baby AGI.

Evaluating agents is difficult; beyond checking final answers, assessing the correctness, efficiency, and appropriateness of intermediate steps (agent trajectories) is important.

Memory plays a crucial role beyond tool interactions, extending to user-agent conversations and agent personalization with long-term memory and evolving objectives or personas. This is explored in recent research on generative agents that simulate complex environments with multiple interacting agents, incorporating memory retrieval weighted by recency, importance, and relevance, and reflection mechanisms that update world states after sequences of actions.

Recent projects building on or extending ReAct include:  
- AutoGPT, which targets open-ended, long-running goals and incorporates long-term memory via vector stores.  
- Baby AGI, which introduced separate planning and execution phases and also uses long-term memory.  
- CAMEL, which focused on multi-agent simulations in chat environments to study interactions and memory without necessarily using external tools.  
- Generative Agents, which simulate a complex environment with many agents interacting, emphasizing memory, reflection, and state updates to produce realistic behaviors.

LangChain incorporates various memory types such as entity memory (building and updating graphs from conversations), knowledge graphs, and summary memories to manage context and state efficiently. Reflection, as a concept for periodically reviewing and updating knowledge, is gaining attention in recent research and may generalize across different memory approaches.

The speaker concludes by inviting questions, acknowledging the field’s early stage and numerous open challenges in making agents reliable and production-ready.</youtube_summary>
)

### What Makes an Agent?

An LLM agent consists of three core components:

1. **LLM Brain**: Makes decisions about what to do next
2. **Tools**: External capabilities the agent can use (e.g., web search, code execution)
3. **Memory**: Retains context across multiple steps

Agents operate through a loop:

- Observe the environment
- Think about what to do
- Take action using tools
- Observe results
- Repeat until task completion

### Command-Line Agent Example

We've created a minimal command-line agent called [`llm-cmd-agent.py`](llm-cmd-agent.py ":ignore") that:

1. Takes a task description from the command line
2. Generates code to accomplish the task
3. Automatically extracts and executes the code
4. Passes the results back to the LLM
5. Provides a final answer or tries again if the execution fails

Here's how it works:

```bash
uv run llm-cmd-agent.py "list all Python files under the current directory, recursively, by size"
uv run llm-cmd-agent.py "convert the largest Markdown file to HTML"
```

The agent will:

1. Generate a shell script to list files with their sizes
2. Execute the script in a subprocess
3. Capture the output (stdout and stderr)
4. Pass the output back to the LLM for interpretation
5. Present a final answer to the user

Under the hood, the agent follows this workflow:

1. Initial prompt to generate a shell script
2. Code extraction from the LLM response
3. Code execution in a subprocess
4. Result interpretation by the LLM
5. Error handling and retry logic if needed

This demonstrates the core agent loop of:

- Planning (generating code)
- Execution (running the code)
- Reflection (interpreting results)
- Adaptation (fixing errors if needed)

### Agent Architectures

Different agent architectures exist for different use cases:

1. **ReAct** (Reasoning + Acting): Interleaves reasoning steps with actions
2. **Reflexion**: Adds self-reflection to improve reasoning
3. **MRKL** (Modular Reasoning, Knowledge and Language): Combines neural and symbolic modules
4. **Plan-and-Execute**: Creates a plan first, then executes steps

### Real-World Applications

LLM agents can be applied to various domains:

1. **Research assistants** that search, summarize, and synthesize information
2. **Coding assistants** that write, debug, and explain code
3. **Data analysis agents** that clean, visualize, and interpret data
4. **Customer service agents** that handle queries and perform actions
5. **Personal assistants** that manage schedules, emails, and tasks

### Project Ideas

Here are some practical agent projects you could build:

1. **Study buddy agent**: Helps create flashcards, generates practice questions, and explains concepts
2. **Job application assistant**: Searches job listings, tailors resumes, and prepares interview responses
3. **Personal finance agent**: Categorizes expenses, suggests budgets, and identifies savings opportunities
4. **Health and fitness coach**: Creates workout plans, tracks nutrition, and provides motivation
5. **Course project helper**: Breaks down assignments, suggests resources, and reviews work

### Best Practices

1. **Clear instructions**: Define the agent's capabilities and limitations
2. **Effective tool design**: Create tools that are specific and reliable
3. **Robust error handling**: Agents should recover gracefully from failures
4. **Memory management**: Balance context retention with token efficiency
5. **User feedback**: Allow users to correct or guide the agent

### Limitations and Challenges

Current LLM agents face several challenges:

1. **Hallucination**: Agents may generate false information or tool calls
2. **Planning limitations**: Complex tasks require better planning capabilities
3. **Tool integration complexity**: Each new tool adds implementation overhead
4. **Context window constraints**: Limited memory for long-running tasks
5. **Security concerns**: Tool access requires careful permission management
