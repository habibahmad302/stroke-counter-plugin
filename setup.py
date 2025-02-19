from setuptools import setup

setup(
    name='plover-stroke-counter',
    version='0.1',
    description='Stroke Counter Plugin for Plover',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    packages=['plover_stroke_counter'],
    entry_points={
        'plover.meta': [
            'stroke_counter = plover_stroke_counter:StrokeCounter'
        ],
    },
    install_requires=['plover>=4.0.0'],
)
