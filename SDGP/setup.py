from setuptools import setup, find_packages

setup(
    name="dynamic-library",
    version="1.0.0",
    description="A library to generate facts and articles using OpenAI's models.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openai",
    ],
    python_requires=">=3.7",
)
