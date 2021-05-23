from random import randint
import exrex


class UserAgent:
    def __init__(self):
        self.patterns = {
            "locales":  ['en-(US|AU|CA|IN|IE|MT|NZ|PH|SG|ZA|GB|US)'],
            "net_clr": {
                "v1":   ['( \\.NET CLR 1\\.[0-1]\\.[4-5]07[0-5][0-9];|)'],
                "v2up": ['( \\.NET CLR [2-3]\\.[1-8]\\.[3-5]07[0-9][0-9];|)']
            },
            "media_server": ['( Media Center PC [4-6]\\.0;|)'],
            "windows": ['Windows NT (6\\.[1-3]|10\\.0)'],
            "macos": {
                "v10_blink":   ['Intel Mac OS X 10_(1[0-4])_[0-4]'],
                "v10_firefox": ['Intel Mac OS X 10\\.(1[0-4])']
            },
            "applewebkit": ['AppleWebKit/(60[1-5]\\.[1-7]\\.[1-8])',
                           'AppleWebKit/(53[5-8]\\.[1-2][0-9]\\.[1-3][0-9])'],
            "browsers_versions": {
                "chrome":  [
                    '(84\\.0\\.4147|83\\.0\\.4103|81\\.0\\.4044)\\.(?:[89]\\d|1[0-4]{2})'],
                "safari":  ['1[23]\\.[0-1]\\.[1-3]'],
                "firefox": ['8[23456]\\.[01]'],
                "opera":   ['6[6789]\\.[0-3]\\.2[1-3][0-9][0-9]\\.([1-2]|)[1-9][0-9]'],
                "edge":    ['Chrome/84\\.0\\.4147\\.89 Safari/537\\.36 Edg/8[23]\\.17763',
                           'Chrome/83\\.0\\.4103\\.116 Safari/537\\.36 Edg/8[23]\\.0\\.416\\.68']
            }
        }

        self.useragents = {
            "ie": {
                "v6": {
                    "name": 'Internet Explorer 6',
                    "regexp": ['Mozilla/4\\.0 \\(compatible; MSIE 6\\.0; Windows NT 5\\.1;( SV1;||)' + self.get_random_array_item(self.patterns['net_clr']['v2up']) + ' ' + self.get_random_array_item(self.patterns['locales']) + '\\)']
                },
                "v7": {
                    "name": 'Internet Explorer 7',
                    "regexp": ['Mozilla/4\\.0 \\((compatible|compatible|Windows; U); MSIE 7\\.0; Windows NT (5\\.1|6\\.0);( WOW64;|)' + self.get_random_array_item(self.patterns['net_clr']['v1']) + self.get_random_array_item(self.patterns['media_server']) + ' InfoPath\\.[1-3]; ' + self.get_random_array_item(self.patterns['locales']) + '\\)']
                },
                "v8": {
                    "name": 'Internet Explorer 8',
                    "regexp": ['Mozilla/4\\.0 \\(compatible; MSIE 8\\.0; Windows NT (5\\.1|6\\.[01]); Trident/4\\.0; (WOW64|WOW64|GTB7\\.[2-6]); InfoPath\\.[2-3];( SV1;|)' + self.get_random_array_item(self.patterns['net_clr']['v1']) + ' ' + self.get_random_array_item(self.patterns['locales']) + '\\)']
                },
                "v9": {
                    "name": 'Internet Explorer 9',
                    "regexp": ['Mozilla/5\\.0 \\((compatible|Windows; U); MSIE 9\\.0; Windows NT 6\\.[01]; (Win64; x64; |WOW64; |)' + 'Trident/5\\.0;' + self.get_random_array_item(self.patterns['net_clr']['v2up']) + self.get_random_array_item(self.patterns['media_server']) + '( Zune 4\\.[0-7];|||)( \\.NET4\\.0(C|E);) ' + self.get_random_array_item(self.patterns['locales']) + '\\)']
                },
                "v10": {
                    "name": 'Internet Explorer 10',
                    "regexp": ['Mozilla/5\\.0 \\(compatible; MSIE 10\\.0; Windows NT 6\\.[12];( InfoPath\\.[2-3];|)' + self.get_random_array_item(self.patterns['net_clr']['v2up']) + ' (WOW64; |)Trident/6\\.0(; ' + self.get_random_array_item(self.patterns['locales']) + '|)\\)']
                },
                "v11": {
                    "name": 'Internet Explorer 11',
                    "regexp": ['Mozilla/5\\.0 \\(' + self.get_random_array_item(self.patterns['windows']) + '; (?:WOW64; )?Trident/7\\.0; "rv":11\\.0\\) like Gecko']
                }
            },
            "edge": {
                "desktop": {
                    "name": 'Edge on Windows',
                    "regexp": ['Mozilla/5\\.0 \\(Windows NT 10\\.0; Win64; x64\\) AppleWebKit/537\\.36 \\(KHTML, like Gecko\\) ' + self.get_random_array_item(self.patterns['browsers_versions']['edge'])]
                },
                "xbox": {
                    "name": 'Edge on Xbox',
                    "regexp": ['Mozilla/5\\.0 \\(Windows NT 10\\.0; Win64; x64; Xbox; Xbox One\\) AppleWebKit/537\\.36 \\(KHTML, like Gecko\\) ' + self.get_random_array_item(self.patterns['browsers_versions']['edge'])]
                }
            },
            "chrome": {
                "win": {
                    "name": 'Chrome on Windows',
                    "regexp": ['Mozilla/5\\.0 \\(' + self.get_random_array_item(self.patterns['windows']) + '(; Win64; x64|; WOW64|)\\) AppleWebKit/537\\.36 \\(KHTML, like Gecko\\) Chrome/(' + self.get_random_array_item(self.patterns['browsers_versions']['chrome']) + ') Safari/537\\.36']
                },
                "mac": {
                    "name": 'Chrome on Mac',
                    "regexp": ['Mozilla/5\\.0 \\(Macintosh; ' + self.get_random_array_item(self.patterns['macos']['v10_blink']) + '\\) AppleWebKit/537\\.36 \\(KHTML, like Gecko\\) Chrome/(' + self.get_random_array_item(self.patterns['browsers_versions']['chrome']) + ') Safari/537\\.36']
                },
                "linux": {
                    "name": 'Chrome on Linux',
                    "regexp": ['Mozilla/5\\.0 \\(X11;( U; | )Linux (x86_64|i686)\\) AppleWebKit/537\\.36 \\(KHTML, like Gecko\\) Chrome/(' + self.get_random_array_item(self.patterns['browsers_versions']['chrome']) + ') Safari/537\\.36']
                }
            },
            "firefox": {
                "win": {
                    "name": 'Firefox on Windows',
                    "regexp": ['Mozilla/5\\.0 \\(' + self.get_random_array_item(self.patterns['windows']) + '; (WOW64|Win64); "rv":(' + self.get_random_array_item(self.patterns['browsers_versions']['firefox']) + ')\\) Gecko/20100101 Firefox/(\\3)']
                },
                "mac": {
                    "name": 'Firefox on Mac',
                    "regexp": ['Mozilla/5\\.0 \\(Macintosh;( U; | )' + self.get_random_array_item(self.patterns['macos']['v10_firefox']) + '; "rv":(' + self.get_random_array_item(self.patterns['browsers_versions']['firefox']) + ')\\) Gecko/20100101 Firefox/(\\3)']
                },
                "linux": {
                    "name": 'Firefox on Linux',
                    "regexp": ['Mozilla/5\\.0 \\(X11; (NetBSD i686|Linux i686|Linux x86_64|Ubuntu; Linux|SunOS sun4u|Gentoo); "rv":(' + self.get_random_array_item(self.patterns['browsers_versions']['firefox']) + ')\\) Gecko/20100101 Firefox/(\\2)']
                },
                "android": {
                    "name": 'Firefox on Android',
                    "regexp": ['Mozilla/5\\.0 \\(Android (?:6\\.0(?:\\.1)?|7\\.(?:0|1(?:\\.[12])?)|8\\.[01]|9\\.0); Mobile; "rv":(' + self.get_random_array_item(self.patterns['browsers_versions']['firefox']) + ')\\) Gecko/\\1 Firefox/\\1']
                }
            },
            "safari": {
                "mac": {
                    "name": 'Safari on Mac',
                    "regexp": ['Mozilla/5\\.0 \\(Macintosh;( U; | )' + self.get_random_array_item(self.patterns['macos']['v10_blink']) + '; ' + self.get_random_array_item(self.patterns['locales']) + '\\) ' + self.get_random_array_item(self.patterns['applewebkit']) + ' \\(KHTML, like Gecko\\) Version/' + self.get_random_array_item(self.patterns['browsers_versions']['safari']) + ' Safari/(\\4)']
                },
                "iphone": {
                    "name": 'Safari on iPhone',
                    "regexp": ['Mozilla/5\\.0 \\(iPhone; U; CPU iPhone OS 11_[0-3]_[0-9] like Mac OS X; ' + self.get_random_array_item(self.patterns['locales']) + '\\) ' + self.get_random_array_item(self.patterns['applewebkit']) + ' \\(KHTML, like Gecko\\) Version/' + self.get_random_array_item(self.patterns['browsers_versions']['safari']) + ' Mobile/8(J|F|C)[1-4](8a|90|) Safari/6533\\.18\\.5']
                },
                "ipad": {
                    "name": 'Safari on iPad',
                    "regexp": ['Mozilla/5\\.0 \\(iPad;( U;|) CPU OS 11_[0-3](_2|) like Mac OS X(; ' + self.get_random_array_item(self.patterns['locales']) + ')\\) ' + self.get_random_array_item(self.patterns['applewebkit']) + ' \\(KHTML, like Gecko\\) Version/' + self.get_random_array_item(self.patterns['browsers_versions']['safari']) + ' Mobile/8(J|F|C)[1-4](8a|90|) Safari/(\\5)']
                }
            },
            "opera": {
                "win": {
                    "name": 'Opera on Windows',
                    "regexp": ['Mozilla/5\\.0 \\(' + self.get_random_array_item(self.patterns['windows']) + '(; Win64; x64|; WOW64|)\\) AppleWebKit/537\\.36 \\(KHTML, like Gecko\\) Chrome/(' + self.get_random_array_item(self.patterns['browsers_versions']['chrome']) + ') Safari/537\\.36 OPR/' + self.get_random_array_item(self.patterns['browsers_versions']['opera'])]
                },
                "mac": {
                    "name": 'Opera on Mac',
                    "regexp": ['Mozilla/5\\.0 \\(Macintosh; ' + self.get_random_array_item(self.patterns['macos']['v10_blink']) + '\\) AppleWebKit/537\\.36 \\(KHTML, like Gecko\\) Chrome/(' + self.get_random_array_item(self.patterns['browsers_versions']['chrome']) + ') Safari/537\\.36 OPR/' + self.get_random_array_item(self.patterns['browsers_versions']['opera'])]
                },
                "linux": {
                    "name": 'Opera on Linux',
                    "regexp": ['Mozilla/5\\.0 \\(X11;( U; | )Linux (x86_64|i686)\\) AppleWebKit/537\\.36 \\(KHTML, like Gecko\\) Chrome/(' + self.get_random_array_item(self.patterns['browsers_versions']['chrome']) + ') Safari/537\\.36 OPR/' + self.get_random_array_item(self.patterns['browsers_versions']['opera'])]
                }
            }
        }

    def get_random_array_item(self, array):
        if type(array) is not list:
            return None
        return array[randint(0, len(array)-1)]

    def get_all_by_key_name(self, object_, key_name):
        result = []

        def recursive(object_, key_name):
            for key in object_:
                if type(object_[key]) is dict:
                    recursive(object_[key], key_name)
                else:
                    if key == key_name:
                        result.append(object_[key])

        recursive(object_, key_name)
        return result

    def test_all_regexp(self):
        regexps = self.get_all_by_key_name(self.useragents, 'regexp')
        length = len(regexps)

        for i in range(length):
            current_regexps = regexps[i]
            current_regexps_count = len(current_regexps)
            print('Testing regexps (' + str(current_regexps_count) + ') "' + str(current_regexps) + '"')  # noqa

            for j in range(current_regexps_count):
                print('> Generate value for regexp: ' + current_regexps[j])

                for _ in range(9):
                    print('>> Generated value: ' + exrex.getone(current_regexps[j]))

    def generate(self, types=None):
        if type(types) is str:
            types = [types]

        if type(types) is not list:
            types = []

        if len(types) <= 0:
            types = ['*']

        regexps = []

        for i in range(len(types)):
            if types[i] == '*':
                return exrex.getone(self.get_random_array_item(self.get_random_array_item(self.get_all_by_key_name(self.useragents, 'regexp'))))

            parts = types[i].split('_')
            major = None
            minor = None

            if type(parts[0]) is str:
                major = parts[0]

            if type(parts[1]) is str:
                major = parts[1]

            if major is not None and minor is not None:
                if major in self.useragents:
                    if minor in self.useragents[major]:
                        regexps.append(self.get_random_array_item(self.useragents[major][minor]['regexp']))
                        continue
        if len(regexps) == 0:
            return None
        return exrex.getone(self.get_random_array_item(regexps))


if __name__ == '__main__':
    ua = UserAgent()
    HEADERS = list(set(ua.generate() for x in range(120)))

    fill = 120 - len(HEADERS)

    while fill != 0:
        HEADERS.extend(list(set(ua.generate() for x in range(fill))))
        HEADERS = list(set(HEADERS))
        fill = 120 - len(HEADERS)
