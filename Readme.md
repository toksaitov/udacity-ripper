udacity-ripper
==============

*udacity-ripper* is a python script that uses Selenium to crawl Udacity
course pages to extract all the lesson YouTube links.

## Prerequisites

* *Python* `>= 2.7`
* *Selenium* `>= 3.8.0`
* Firefox, geckodriver `>= 57.0.1`, `>= 0.19.1`

# Usage

Install Firefox and the geckodriver first.

```bash
pip install -r requirements.txt
python udacity-ripper.py <CLASS URL> <LOGIN> <PASSWORD>
```

## Licensing

*udacity-ripper* is licensed under the MIT license. See LICENSE for the full
license text.

## Credits

*udacity-ripper* was created by [Dmitrii Toksaitov](https://github.com/toksaitov).

