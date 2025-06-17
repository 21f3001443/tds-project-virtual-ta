## Serverless hosting: Vercel

<!--

Why Vercel? I evaluated from https://survey.stackoverflow.co/2024/technology#2-cloud-platforms

- AWS, Azure, Google Cloud are too complex for beginners
- Cloudflare (next most popular, widely admired) Python support is in beta
- Hetzner (most admired), Supabase (next most admired) do not have a serverless platform
- Fly.io (next most admired) does not have a free tier
- Heroku (used in previous terms) is the least admired
- Vercel is both popular, admired, growing, has a free plan, and a simple API

-->

Serverless platforms let you rent a single function instead of an entire machine. They're perfect for small web tools that _don't need to run all the time_. Here are some common real-life uses:

- A contact form that emails you when someone wants to hire you (runs for 2-3 seconds, a few times per day)
- A tool that converts uploaded photos to black and white (runs for 5-10 seconds when someone uploads a photo)
- A chatbot that answers basic questions about your business hours (runs for 1-2 seconds per question)
- A newsletter sign-up that adds emails to your mailing list (runs for 1 second per sign-up)
- A webhook that posts your Etsy sales to Discord (runs for 1 second whenever you make a sale)

You only pay when someone uses your tool, and the platform automatically handles busy periods. For example, if 100 people fill out your contact form at once, the platform creates 100 temporary copies of your code to handle them all. When they're done, these copies disappear. It's cheaper than running a full-time server because you're not paying for the time when no one is using your tool - most tools are idle 95% of the time!

Rather than writing a full program, serverless platforms let you write functions. These functions are called via HTTP requests. They run in a cloud environment and are scaled up and down automatically. But this means you write programs in a different style. For example:

- You can't `pip install` packages - you have to use `requirements.txt`
- You can't read or write files from the file system - you can only use APIs.
- You can't run commands (e.g. `subprocess.run()`)

[Vercel](https://vercel.com/) is a cloud platform optimized for frontend frameworks and serverless functions. Vercel is tightly integrated with GitHub. Pushing to your repository automatically triggers new deployments.

Here's a [quickstart](https://vercel.com/docs/functions/runtimes/python). [Sign-up with Vercel](https://vercel.com/signup). Create an empty `git` repo with this `api/index.py` file.

To deploy a FastAPI app, add a `requirements.txt` file with `fastapi` as a dependency.

```text
fastapi
```

Add your FastAPI code to a file, e.g. `main.py`.

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

Add a `vercel.json` file to the root of your repository.

```json
{
  "builds": [{ "src": "main.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "main.py" }]
}
```

On the command line, run:

- `npx vercel` to deploy a test version
- `npx vercel --prod` to deploy to production

**Environment Variables**. Use `npx vercel env add` to add environment variables. In your code, use `os.environ.get('SECRET_KEY')` to access them.

### Videos

[![Vercel Product Walkthrough](https://i.ytimg.com/vi_webp/sPmat30SE4k/sddefault.webp)](https://youtu.be/sPmat30SE4k
<youtube_summary>In this video walkthrough, Lee introduces the Vercel platform, a Frontend Cloud that supports over 35 frameworks including React, Svelte, and Next.js (which Vercel created). Starting with deploying a Next.js template from Vercel's marketplace, Lee demonstrates the seamless integration with GitHub (also supporting GitLab and Bitbucket), where Vercel automatically creates a repository, links it to the project, and initiates a CI/CD pipeline that builds and deploys the app globally via Vercel's Edge Network within about 30-40 seconds.

The platform auto-detects frameworks, runs build commands, and uploads static assets and serverless functions for dynamic compute. Lee reviews the deployment dashboard showing details like framework version, deployed assets, and functions. He also showcases updating the app by editing code in GitHub, committing changes, and Vercel automatically triggering new deployments for both production and preview environments.

Vercel supports pull request workflows with preview deployments that include a built-in commenting system allowing team members to annotate UI elements directly on the live preview, facilitating collaborative reviews before merging to production. Comments can block merges until resolved. Once approved, merging to the main branch triggers a production deployment with updated code live on the assigned domain.

The platform differentiates between deployment (local), preview (branch-specific environments), and production environments, allowing environment-specific variables to be set and accessed dynamically in code using process.env. Environment variables can be managed in the dashboard and scoped per environment.

Additional features include domain management (purchasing or adding custom domains), detailed request logs with filtering options, and advanced monitoring tools for querying traffic and performance data. Vercel offers a privacy-friendly Web Analytics product for visitor insights and a Speed Insights tool to monitor real-user performance, core web vitals, and detect regressions, with the ability to instantly rollback deployments if needed.

For content-driven sites, Vercel integrates with multiple CMS platforms (Contentful, Sanity, Builder, Tina, Dato, Payload) enabling inline visual editing of draft content directly on the deployed preview, linking back to the CMS for seamless content management.

Vercel also provides built-in storage options including KV stores, Postgres databases, blob/object storage, and Edge Config for low-latency data access globally. Creating databases is simple via the dashboard, with support for popular integrations like Prisma and native drivers.

The platform supports numerous third-party integrations (e.g., PlanetScale, Shopify, Sitecore) through templates and an integrations marketplace, facilitating rapid development of complex applications such as e-commerce sites. For custom needs, Vercel offers a REST API and CLI for full platform extensibility.

Lee concludes by encouraging viewers to subscribe and engage with feedback on features they want to learn more about. Vercel's pricing plans include a free tier for side projects, Pro accounts for teams with higher usage limits, and Enterprise plans offering advanced features like audit logs, SAML SSO, IP blocking, and custom domain suffixes.

Overall, Vercel streamlines frontend development by combining framework support, automated CI/CD, global edge deployment, collaborative preview environments, real-time logs and analytics, easy database provisioning, rich integrations, and strong performance monitoring into one platform.</youtube_summary>
)

[![Deploy FastAPI on Vercel | Quick and Easy Tutorial](https://i.ytimg.com/vi_webp/8R-cetf_sZ4/sddefault.webp)](https://youtu.be/8R-cetf_sZ4
<youtube_summary>This video demonstrates the fastest way to deploy a Python FastAPI application online using Vercel, entirely for free. The process involves three steps: creating a new Vercel account, adding a FastAPI app to it, and deploying the app.

Steps covered:
1. Create a new folder named "API" and inside it, create a "main.py" file with a simple FastAPI app containing a health check endpoint that returns "health check is successful."
2. Create a "requirements.txt" file listing the dependencies: fastapi and uvicorn.
3. Create a "vercel.json" file to configure the build and routes, specifying the source as "API/main.py" and using the latest Python version (default in Vercel).

Next, sign up for a free Vercel account (Hobby tier). Install Node.js and then install the Vercel CLI globally using `npm i -g vercel`. Log in to Vercel through the CLI. Run `vercel .` in the project directory, answer prompts to link to the project, and deploy.

If the deployed app is down due to a current Vercel bug, fix it by:
- Going to the Vercel dashboard settings for the project,
- Changing the Node.js version to 18.x,
- Saving and redeploying using `vercel .`.

After redeployment, open the latest deployment URL to see the live FastAPI app responding successfully to the health check. The entire process is quick, easy, and free. The video also suggests additional resources for learning more about FastAPI.</youtube_summary>
)
