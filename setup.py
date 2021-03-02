setup(
    name="vo_recorder",
    version="1.0.0",
    description="A simple recorder for scripted voice-over",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/simonpauw/vo_recorder",
    author="Simon Pauw",
    author_email="info@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["vo_recorder"],
    include_package_data=True,
    install_requires=[
        "pyaudio", "wave", "pathlib", "os", "pynput", "msvcrt", "colorama", "cursor"
    ],
    entry_points={"console_scripts": ["vorec=vo_recorder.__init__:main"]},
)
