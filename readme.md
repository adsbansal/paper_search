# 360 - Research Papers 👨‍🔬   

Welcome to 360 - Research Papers, a generative AI app that helps you kickstart your research paper writing journey! 📝    

## Overview 🚀   

360 - Research Papers is an application that assists users in generating research paper topics and provides a brief overview of the chosen topic. It also curates a list of recent high-citation papers related to the topic and provides YouTube links to get you started on your research. 📚   

## Getting Started 🛠️   

To use the 360 - Research Papers app, follow these steps:

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/adsbansal/paper_search.git
   ```

2. Navigate to the project directory:

   ```shell
   cd paper_search
   ```

3. Install the required dependencies using pip:

   ```shell
   pip install -r requirements.txt
   ```

4. Obtain your OpenAI API key from [OpenAI](https://platform.openai.com/signup) and replace `YOUR_API_KEY` in `external.py` with your actual API key.

5. Run the app locally with the following command:

   ```shell
   streamlit run external.py
   ```

## Project Tree 🌳   

Here's a glimpse of the project structure:

```
paper_search
   ├── TestingNotebooks
   │   ├── custom-tools.ipynb
   │   └── tests.ipynb
   ├── Tools
   │   ├── __pycache__
   │   │   ├── google_scholar.cpython-310.pyc
   │   │   └── youtube_search.cpython-310.pyc
   │   ├── google_scholar.py
   │   └── youtube_search.py
   ├── __pycache__
   │   └── internal.cpython-310.pyc
   ├── external.py
   ├── internal.py
   ├── readme.md
   └── results.txt
```

## Usage 📖

1. Run the app using the `streamlit` command.
2. Enter the topic you want to write a research paper on.
3. Click "Generate" to get a brief overview and access recent high-citation papers.
4. Explore the provided YouTube links to start your research journey.

## Contributing 🤝

We welcome contributions to make 360 - Research Papers even better! If you'd like to contribute, please fork the repository and create a pull request with your changes.

## Issues and Feedback 🙋‍♀️

If you encounter any issues or have feedback, please feel free to open an issue on the [GitHub repository](https://github.com/adsbansal/paper_search.git).

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Happy researching! 🧪📊🔬
