'''
 * Author: Lukasz Jachym
 * Date: 11/29/14
 * Time: 5:48 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''
import sys

import pysentiment as ps

hiv4 = ps.HIV4()
lm = ps.LM()

text = sys.stdin.read()


hiv4_tokens = hiv4.tokenize(text)
lm_tokens = lm.tokenize(text)

hiv4_score = hiv4.get_score(hiv4_tokens)
lm_score = lm.get_score(lm_tokens)

print('HIV4 score: %s' % hiv4_score)
print('LM score: %s' % lm_score)