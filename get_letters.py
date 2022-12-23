"""================================================================================================
This script accesses each 'Letter to Shareholders' from Berkshire Hathaway's online archive.

12/23/22   Ben Iovino   WarrenLetters
================================================================================================"""

import requests
from bs4 import BeautifulSoup


def main():

    # All letters under same url structure
    url = 'https://www.berkshirehathaway.com/letters/'
    html_letters = ['1977.html', '1978.html', '1979.html', '1980.html', '1981.html', '1982.html',
        '1983.html', '1984.html', '1985.html', '1986.html', '1987.html', '1988.html', '1989.html',
        '1990.html', '1991.html', '1992.html', '1993.html', '1994.html', '1995.html', '1996.html',
        '1997.html']
    pdf_letters = ['1998pdf.pdf', '1999pdf.pdf', '2000pdf.pdf', '2001pdf.pdf', '2002pdf.pdf',
        '2003ltr.pdf', '2004ltr.pdf', '2005ltr.pdf', '2006ltr.pdf', '2007ltr.pdf', '2008ltr.pdf',
        '2009ltr.pdf', '2010ltr.pdf', '2011ltr.pdf', '2012ltr.pdf', '2013ltr.pdf', '2014ltr.pdf',
        '2015ltr.pdf', '2016ltr.pdf', '2017ltr.pdf', '2018ltr.pdf', '2019ltr.pdf', '2020ltr.pdf',
        '2021ltr.pdf']

    # Get content of webpage
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
    result = requests.get(url+pdf_letters[10], headers=headers, timeout=10)

    # Take words from requests result
    letter = BeautifulSoup(result.content, 'html.parser')
    print(result.content)


if __name__ == '__main__':
    main()
