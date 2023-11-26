# summary4.py
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

class TextSummarizer:
    def __init__(self, model_name='facebook/bart-large-cnn'):
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, text, max_length=130, min_length=30, length_penalty=2.0, num_beams=4):
        # Encode the text, add the necessary tokens, and generate the summary
        inputs = self.tokenizer.encode("summarize: " + text, return_tensors='pt', max_length=1024, truncation=True)
        summary_ids = self.model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=length_penalty, num_beams=num_beams)
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Example usage
text = """
Your guide to planetary energies 
November 13 to 19, 2023
﻿By Astrologer Pam Younghans
​
SCORPIO NEW MOON: A new lunar cycle begins at 1:27 a.m. PST this Monday, November 13, when the Sun and Moon align at 20°43' Scorpio. The eighth sign of the zodiac is ruled by both the Scorpion and the Eagle, symbolizing the lower-frequency and the higher-vibrational qualities of the sign. With every sign, we have a choice of whether to take the high road or the low road, but our options with Scorpio can be especially clear and compelling.
 
This New Moon may evoke intense or complex reactions, perhaps because we must deal with situations or emotions that feel outside of our control. We can feel an urgent need to solve a mystery or to uncover a truth that has been elusive. Psychic perceptions are strengthened, as is our capacity for diving more deeply into our own psyches to understand our desires and motivations.
 
If we encounter emotions such as resentment or fear, or self-destructive behaviors such as addictions or extreme reactivity, Scorpio then supports a deep cleansing and release, a death of the old and a rebirth into new form. This process is embodied by another animal symbol linked to the sign, the mythical Phoenix, which is consumed by fire and then rises anew from the ashes.
 
Issues of power and control are another theme to expect with a Scorpio lunar cycle. Extremes of both the light and the shadow in ourselves and in the world around us are likely to be quite apparent. 
 
MARS-URANUS EFFECT: At the time of Monday's New Moon, the Sun and Moon will be closely conjunct Mars and very tightly opposite Uranus in Taurus. This means that the energies of the unsettling Mars-Uranus opposition that was exact on November 11 are strongly reactivated by the lunation. Those energies will also be woven into our experience of the next two to four weeks.
 
There is restlessness and uncertainty whenever we are working with sideways-spinning Uranus. As the planet is activated, we can experience situations that seem random or are in some way surprising. Nervous energy is heightened, which can be unsettling to our mental, emotional, and physical bodies. If we feel anxious, it may help to ponder how similarly our bodies feel fear and excitement; it is the label that our minds place on the feeling that determines how we perceive it.
 
As the New Moon triggers the Mars-Uranus opposition, actions and reactions can be instinctive and unexpected. If we feel irritations and frustrations building, it will be wise to release them in small increments so that they do not reach a crisis point. We can also benefit from remembering that Uranus is the planet of Liberation. It may be presenting us with unexpected events to help free us from old patterns and routines. It may also be provoking strong emotions that have been unconscious until now, bringing them into our awareness so that they no longer control us from behind the scenes.
 
As always with Uranian aspects, grounding and connection to the Earth are recommended. Being in touch with Nature can help disperse the energy so that our nervous system does not become overwhelmed.
 
SAGITTARIUS SOLAR MONTH CLASS: My Solar Month Class covering the month of Sagittarius is set for Wednesday, November 22! To learn more, visit https://events.humanitix.com/solar-month-class-sagittarius-2023

INSTAGRAM: I invite you to check out my daily astrological updates on Instagram! https://www.instagram.com/pamyounghans/ 

DAILY ASPECTS: Here are my brief interpretations of this week's most important planetary aspects: 
 
Monday
New Moon: The Sun and Moon align at 1:27 a.m. PST (1927 UT) today. This New Moon marks the beginning of a very eventful lunar cycle that encourages change on deep levels and will serve to liberate us in some way.
Sun opposite Uranus: The Sun is exactly opposite Uranus eight hours after the New Moon occurs. This is a very rebellious influence, and we are unlikely to have much patience with anything that is outside of our control or that limits our freedom.
Venus sesquiquadrate Uranus: Changes in relationship or financial situations are driven by a need for more freedom and equality. 
 
Tuesday
No major aspects are exact today.
 
Wednesday
Mercury sextile Venus, Sun semisquare Venus: We are drawn to share our perspective with a friend or loved one, but may experience discomfort over how much to reveal of our true feelings.
Mercury quincunx Jupiter, Venus quincunx Jupiter: These aspects, along with the Mercury-Venus sextile, together form a configuration called a "yod." It places emphasis on the need to shift a perspective or discard a belief that has become stagnant and outdated.
 
Thursday
Mars quincunx Eris, Mercury sesquiquadrate Eris, Sun quincunx Eris: With the goddess of Discontent in hard aspect to three other planets today, people may be especially reactive and defensive. A demand for attention and the need to assert one's personal rights are especially strong.
 
Friday
Mars trine Neptune, Sun trine Neptune, Sun conjunct Mars: Personal will is active, but is well-informed by intuition and by higher ideals. This can be a very good day for taking on a new creative endeavor or making a spiritual breakthrough. Actions are motivated by compassion and the desire to understand profound universal truths.
 
Saturday
Mercury semisquare Pluto: Differences of opinion may interfere with our ability to fully trust others. Some may respond to disagreements with self-righteous indignation.
 
Sunday
No major aspects are exact today.
 
IF YOUR BIRTHDAY IS THIS WEEK: Your need for new experiences is especially strong in the year ahead. As a result, you may feel very restless and impatient with anything that seems stale or routine, or too safe. If you attempt to contain or ignore these feelings, they can build up until they are expressed haphazardly or impulsively. However, if you give yourself many opportunities to try new things this year, they will ultimately open the door to a new life and a new self-concept. As significant side benefits of your journey through the coming year, your spiritual life is enhanced and your sense of purpose becomes more clear. (Solar Return Sun semisquare Venus, conjunct Mars, opposite Uranus, trine Neptune, sextile Pluto)
​
In peace, love, and gratitude,
 
Pam
"""

summarizer = TextSummarizer()
summary = summarizer.summarize(text)
print(summary)
