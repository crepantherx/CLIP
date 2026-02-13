from pathlib import Path
from setuptools import setup, find_packages


BASE_DIR = Path(__file__).parent


def load_requirements():
    requirements_file = BASE_DIR / "requirements.txt"
    with requirements_file.open() as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]


setup(
    name="clip",
    version="1.0",
    description="CLIP model by OpenAI",
    author="OpenAI",
    packages=find_packages(exclude=["tests*"]),
    py_modules=["clip"],
    install_requires=load_requirements(),
    include_package_data=True,
    extras_require={
        "dev": ["pytest"],
    },
)
