
---

# 🤖 GitHub Copilot Inline Code Suggestions in VS Code

## What is Inline Code Suggestion?

GitHub Copilot can suggest code **directly inside your editor while you type**.

The suggestion usually appears as faded or **ghost text**.

Example:

```python
def calculate_area(length, width):
```

Copilot may suggest:

```python
def calculate_area(length, width):
    return length * width
```

You can usually press **`Tab`** to accept the suggestion. VS Code describes these as **ghost text suggestions**, alongside newer **next edit suggestions**. ([Visual Studio Code][1])

---

# ✅ Prerequisites

Before using GitHub Copilot inline suggestions, make sure you have:

1. **Visual Studio Code installed**
2. A **GitHub account**
3. Access to **GitHub Copilot**
4. Signed in to GitHub inside VS Code
5. Copilot/AI features enabled in VS Code

GitHub Copilot access can include the Copilot Free plan, which provides a monthly allowance of inline suggestions and AI credits. ([Visual Studio Code][1])

---

# 🚀 How to Enable Inline Code Suggestions

## Method 1: Using VS Code Settings

### Step 1: Open Settings

On Mac:

```text
⌘ + ,
```

On Windows/Linux:

```text
Ctrl + ,
```

### Step 2: Search for:

```text
github.copilot.enable
```

You will see settings similar to:

| Language    | Value   |
| ----------- | ------- |
| `*`         | `true`  |
| `plaintext` | `false` |
| `markdown`  | `false` |
| `scminput`  | `false` |

Make sure:

```text
* → true
```

This enables Copilot inline suggestions for languages generally, unless a specific language is configured differently. ([GitHub Docs][2])

---

# 🐍 Enable Copilot Specifically for Python

You can configure Copilot using `settings.json`.

Example:

```json
{
    "github.copilot.enable": {
        "*": true,
        "python": true,
        "plaintext": false,
        "markdown": false
    }
}
```

This means:

```text
* → Enable Copilot generally
python → Explicitly enable for Python
plaintext → Disable for plain text files
markdown → Disable for Markdown files
```

VS Code supports enabling or disabling Copilot inline suggestions globally or for individual languages. ([GitHub Docs][2])

---

# ⛔ How to Disable Inline Suggestions

## Disable for All Languages

Open `settings.json` and use:

```json
{
    "github.copilot.enable": {
        "*": false
    }
}
```

This disables Copilot inline suggestions for all languages. GitHub's learning documentation also uses this approach for disabling suggestions within a project. ([GitHub Docs][3])

---

# 🐍 Disable Only for Python

If you want Copilot to work everywhere except Python:

```json
{
    "github.copilot.enable": {
        "*": true,
        "python": false
    }
}
```

This is useful if you are teaching or practicing Python and want to write the code yourself.

---

# 💤 Temporarily Disable Suggestions

VS Code also lets you **snooze** inline suggestions temporarily.

From the Copilot menu/status controls, you can snooze suggestions and later cancel the snooze. You can also use the Command Palette commands:

```text
Snooze Inline Suggestions
```

and:

```text
Cancel Snooze Inline Suggestions
```

This is useful when you don't want to change your permanent settings. ([Visual Studio Code][1])

---

# ✍️ How to Use Inline Suggestions

Open a Python file and start typing:

```python
def calculate_bmi(weight, height):
```

Copilot may suggest:

```python
    return weight / (height ** 2)
```

The suggestion appears as **faded/ghost text**.

### To accept the suggestion:

```text
Tab
```

---

# 🧪 Test Example

Create a Python file:

```python
# Calculate the area of a rectangle
```

Then pause for a moment.

Copilot may suggest:

```python
def calculate_area(length, width):
    return length * width
```

You can:

* Press `Tab` → Accept the suggestion
* Continue typing → Modify the suggestion
* Ignore it → Copilot may generate another suggestion

---

# ⚙️ Important Settings

## 1. Enable or Disable Copilot Completions

```text
github.copilot.enable
```

Controls whether Copilot provides inline suggestions globally or for specific languages.

Example:

```json
"github.copilot.enable": {
    "*": true,
    "python": true
}
```

---

## 2. Enable Next Edit Suggestions

```text
github.copilot.nextEditSuggestions.enabled
```

This controls **Next Edit Suggestions**, where Copilot predicts your next likely code change, potentially even at another location in the file. ([Visual Studio Code][1])

Example:

```json
{
    "github.copilot.nextEditSuggestions.enabled": true
}
```

---

# 🔍 If Copilot Suggestions Are Not Appearing

Check these things:

### 1. Is Copilot enabled?

Search:

```text
github.copilot.enable
```

Make sure:

```text
* → true
```

---

### 2. Is Python specifically disabled?

Check whether you have:

```text
python → false
```

If yes, change it to:

```text
python → true
```

---

### 3. Are you signed in?

Make sure VS Code recognizes your GitHub account and Copilot access.

---

### 4. Is your Copilot plan active?

VS Code notes that inline suggestions may not work if your Copilot subscription is not active or, on Copilot Free, if the monthly inline suggestion limit has been reached. ([Visual Studio Code][4])

---

### 5. Check your internet connection

Copilot requires connectivity to provide cloud-based suggestions.

---

# 📌 Recommended Setup

For someone learning and teaching Python, a good setup is:

```json
{
    "github.copilot.enable": {
        "*": true,
        "python": true,
        "plaintext": false,
        "markdown": false,
        "scminput": false
    },
    "github.copilot.nextEditSuggestions.enabled": true
}
```

This gives you Copilot suggestions while coding Python without enabling them unnecessarily in plain text, Markdown, or commit-message input.

---

# ⚡ Quick Cheat Sheet

| Situation                    | What to do                                         |
| ---------------------------- | -------------------------------------------------- |
| Enable Copilot everywhere    | `"*": true`                                        |
| Disable Copilot everywhere   | `"*": false`                                       |
| Enable only Python           | `"python": true`                                   |
| Disable Python               | `"python": false`                                  |
| Accept suggestion            | `Tab`                                              |
| Enable Next Edit Suggestions | `github.copilot.nextEditSuggestions.enabled: true` |
| Temporarily stop suggestions | Snooze Inline Suggestions                          |
| Turn suggestions back on     | Cancel Snooze Inline Suggestions                   |

---

**Official references:** [VS Code – Inline Suggestions from GitHub Copilot](https://code.visualstudio.com/docs/editing/ai-powered-suggestions?utm_source=chatgpt.com) · [GitHub Docs – Configure Copilot in VS Code](https://docs.github.com/en/copilot/how-tos/configure-personal-settings/configure-in-ide?utm_source=chatgpt.com)

[1]: https://code.visualstudio.com/docs/editing/ai-powered-suggestions?utm_source=chatgpt.com "Inline suggestions from GitHub Copilot in VS Code"
[2]: https://docs.github.com/en/copilot/how-tos/configure-personal-settings/configure-in-ide?utm_source=chatgpt.com "Configuring GitHub Copilot in your environment - GitHub Docs"
[3]: https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code?utm_source=chatgpt.com "Setting up Copilot for learning to code - GitHub Docs"
[4]: https://code.visualstudio.com/docs/agents/agent-troubleshooting/faq?utm_source=chatgpt.com "GitHub Copilot frequently asked questions"
