/* Extended Essay hub — sample essay data.
   Used by samples/index.html.

   Three sources:
   "m27"   IB example essays for first assessment 2027, marked /30 on the 2027 criteria.
           PDFs copied into samples/files/ (essay, examiner marks, RPF — not every sample has all three).
   "ibo"   IB public examples (written under the previous guide, re-marked by the IB on the 2027 criteria, /30).
           Hosted by the IB — we link to the IB's own URLs. Mark known only where Michael checked the commentary.
   "old"   IB examples from the previous guide's app (rubric /34, different criteria). Hosted by the IB.

   Letter grades are ESTIMATES. /30 cut-offs come from the school's Rubric & Supervisor Guide
   (indicative, not IB-published); /34 cut-offs are the ones schools commonly report for the old rubric.
   Update this file when the IB publishes official 2027 boundaries.

   To add a sample: copy one object, change the fields, save. */

window.EE_BOUNDARIES = {
  30: [["A",24],["B",19],["C",14],["D",7],["E",0]],
  34: [["A",27],["B",21],["C",14],["D",7],["E",0]]
};

window.EE_SAMPLES = [
  /* ── 2027 examples (files in samples/files/) ── */
  {src:"m27", subject:"Biology", id:"biology-a", label:"Sample A", rq:"An investigation into the effect of alcohol production ln different yeast strains during the fermentation of wine.", marks:{A:4,B:4,C:4,D:6,E:3}, total:21, outOf:30, files:["marks","rpf"]},
  {src:"m27", subject:"Biology", id:"biology-c", label:"Sample C", rq:"To what extent do monosodium glutamate, sucralose, carboxymethylcellulose, and sodium benzoate affect the survival of Lactobacillus acidophilus?", marks:{A:4,B:5,C:5,D:7,E:4}, total:25, outOf:30, files:["marks"]},
  {src:"m27", subject:"Business Management", id:"business-management-a", label:"Sample A", rq:"How has incorporating Corporate Social Responsibility principles into its business operations helped Starbucks to increase its revenue globally?", marks:{A:5,B:6,C:6,D:3,E:2}, total:22, outOf:30, files:["marks","rpf"]},
  {src:"m27", subject:"Business Management", id:"business-management-c", label:"Sample C", rq:"To what extent is PayPal’s success attributed to its differentiation strategies?", marks:{A:4,B:5,C:3,D:2,E:3}, total:17, outOf:30, files:["marks","rpf"]},
  {src:"m27", subject:"Chemistry", id:"chemistry-a", label:"Sample A", rq:"Is acetaminophen as effective as aspirin (acetylsalicylic acid) as an inhibitor of cyclooxigenase-1 (COX-1) catalysis of arachidonic acid metabolism, determined by calculating the IC50 values?", marks:{A:5,B:4,C:6,D:6,E:2}, total:23, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Chemistry", id:"chemistry-b", label:"Sample B", rq:"How effectively can chitosan chemically remove Pb from H2O, compared to activated carbon?", marks:{A:4,B:5,C:4,D:4,E:2}, total:19, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Design Technology", id:"design-technology-a", label:"Sample A", rq:"Can compostable materials be a sustainable solution to how the fields of mass manufactured EPS food packaging contributed to the world’s environmental causes?", marks:{A:2,B:2,C:3,D:3,E:1}, total:11, outOf:30, files:["marks","rpf"]},
  {src:"m27", subject:"Design Technology", id:"design-technology-c", label:"Sample C", rq:"With reference to structural integrity and environmental consideration, what would be the most suitable cement alternatives for the construction of stabilized rammed earth structures?", marks:{A:5,B:5,C:4,D:4,E:4}, total:22, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Economics", id:"economics-b", label:"Sample B", rq:"To what extent has the mínimum price per unit in Scotland been effective in reducing consumption and demand for alcohol since 2018?", marks:{A:4,B:4,C:4,D:6,E:2}, total:20, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Economics", id:"economics-d", label:"Sample D", rq:"What effect have the Labour Board and Union Had on the Wages and Wellbeing of Mathadi Workers in the Mumbai Agricultural Produce Market Committee (APMC)?", marks:{A:3,B:3,C:3,D:4,E:2}, total:15, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"ESS", id:"ess-a", label:"Sample A", rq:"To what extent do the inputs and outputs of water at the Dead Sea, Israel, allow a sustainable withdrawal of water by the chemical industry from 2000 to 2020?", marks:{A:3,B:4,C:4,D:3,E:3}, total:17, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"ESS", id:"ess-c", label:"Sample C", rq:"How far is the enhanced infiltration of UVA radiation (315-400nm) due to ozone depletion less detrimental than UVB (280-315nm) for the germination and growth of Gerbera (Gerbera L.) and Chamomile (Matricaria chamomilla) flowering plants?", marks:{A:6,B:6,C:5,D:7,E:4}, total:28, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"History", id:"history-c", label:"Sample C", rq:"How significant was the 1968 Tet Offensive in causing US failure in the Vietnam War?", marks:{A:4,B:4,C:3,D:4,E:1}, total:16, outOf:30, files:["marks","rpf"]},
  {src:"m27", subject:"History", id:"history-d", label:"Sample D", rq:"To what extent did prolonged unequal US-Cuban relations produce the conditions for revolution in Cuba between 1895-1953?", marks:{A:3,B:4,C:4,D:4,E:3}, total:18, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Interdisciplinary", framework:"Culture, identity, expression", id:"interdisciplinary-cie-c", label:"Sample C", rq:"How does the televisión programme Pingu utilise nonverbal communication in order to tell a story which can be understood by a global audience?", marks:{A:2,B:2,C:2,D:3,E:3}, total:12, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Interdisciplinary", framework:"Power, equality, justice", id:"interdisciplinary-pej-b", label:"Sample B", rq:"To what extent does the characterisation of females in the James Bond film Skyfall reflect concepts of ambivalent sexism?", marks:{A:4,B:5,C:4,D:4,E:2}, total:19, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Interdisciplinary", framework:"Power, equality, justice", id:"interdisciplinary-pej-d", label:"Sample D", rq:"How effective are microfinance institutions in reducing gender inequalities in low-income countries?", marks:{A:4,B:4,C:4,D:6,E:3}, total:21, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Language A", id:"language-a-b", label:"Sample B", rq:"How does Orwell use setting to communicate the dangers of a totalitarian society?", marks:{A:3,B:4,C:4,D:4,E:3}, total:18, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Language A", id:"language-a-d", label:"Sample D", rq:"In what ways does Wilbur Soot utilize his lyrics to convey the message that systematic ignorance perpetuates the mental health crisis?", marks:{A:5,B:4,C:5,D:5,E:2}, total:21, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Language B", id:"language-b-a", label:"Sample A", rq:"To what extent do the Disney movies “Cinderella” and “Beauty and the Beast” show the change of perception of women from different time periods?", marks:{A:3,B:4,C:4,D:5,E:3}, total:19, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Language B", id:"language-b-b", label:"Sample B", rq:"To what extent does Emily Bronte’s portrayal of female characters in her novel Wuthering Heights indicate that she was a proto-feminist?", marks:{A:5,B:5,C:5,D:5,E:3}, total:23, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Mathematics", id:"mathematics-a", label:"Sample A", rq:"What is the surface area to which a goat has access?", marks:{A:3,B:4,C:4,D:4,E:2}, total:17, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Mathematics", id:"mathematics-c", label:"Sample C", rq:"Which is the most efficient method of calculating π?", marks:{A:4,B:4,C:5,D:5,E:2}, total:20, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Physics", id:"physics-b", label:"Sample B", rq:"How does the impact speed of a sphere affect the size of the crater when collide with the flour surface?", marks:{A:5,B:4,C:4,D:4,E:3}, total:20, outOf:30, files:["marks","rpf"]},
  {src:"m27", subject:"Physics", id:"physics-d", label:"Sample D", rq:"How do different types of Stirling engines contribute to energy generated and efficiency?", marks:{A:2,B:3,C:2,D:2,E:2}, total:11, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Psychology", id:"psychology-a", label:"Sample A", rq:"To what extent does listening to music lessen the symptoms of ADHD?", marks:{A:5,B:4,C:4,D:4,E:1}, total:18, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Psychology", id:"psychology-b", label:"Sample B", rq:"To what extent is there a relationship between self-efficacy and performance in acrobatic sports?", marks:{A:6,B:5,C:6,D:4,E:3}, total:24, outOf:30, files:["marks","rpf"]},
  {src:"m27", subject:"Theatre", id:"theatre-a", label:"Sample A", rq:"How does lighting within the National Theatre's Frankenstein affect an audience's perception of the play?", marks:{A:6,B:5,C:5,D:6,E:2}, total:24, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Theatre", id:"theatre-b", label:"Sample B", rq:"How does ‘Soldaat van Oranje – De Musical’ use scenography to evoke the feeling of Dutch national unity and pride among the audience?", marks:{A:6,B:5,C:6,D:5,E:4}, total:26, outOf:30, files:["essay","marks"]},
  {src:"m27", subject:"Visual Arts", id:"visual-arts-a", label:"Sample A", rq:"To what extent have Clara Peeter’s Flemish Still Life paintings influenced Post Contemporary artists Rebecca Ruetten and Audrey Flack?", marks:{A:4,B:5,C:4,D:4,E:3}, total:20, outOf:30, files:["essay","marks","rpf"]},
  {src:"m27", subject:"Visual Arts", id:"visual-arts-b", label:"Sample B", rq:"How did the use of unconventional materials in the Works of Magdalena Abakanowicz and Eva Hesse influence their process to express meaning?", marks:{A:5,B:5,C:5,D:4,E:3}, total:22, outOf:30, files:["essay","marks","rpf"]},

  /* ── IB public examples, re-marked on the 2027 criteria (hosted by the IB) ── */
  {src:"ibo", subject:"Language A", code:"langa", n:1, rq:"How do themes present in Sylvia Plath's 1963 The Bell Jar portray Esther Greenwood's development of psychotic depression?"},
  {src:"ibo", subject:"Language A", code:"langa", n:2, rq:"How does Ernest Hemingway's literary style reflect through motifs and character development present in A Farewell to Arms?"},
  {src:"ibo", subject:"Language A", code:"langa", n:3, rq:"How does Ayn Rand use The Fountainhead to show how objectivism plays out in societal, economic and political arenas?"},
  {src:"ibo", subject:"Language B", code:"langb", n:1, rq:"How do Arthur Conan Doyle and Agatha Christie develop different version of the crime genre?"},
  {src:"ibo", subject:"Language B", code:"langb", n:2, rq:"To what extent do the writers of the film Green Book use the contrast between the protagonists to reflect racial discrimination in the southern part of the United States in the 1960s?"},
  {src:"ibo", subject:"Language B", code:"langb", n:3, rq:"How does Trainspotting's realism reflect the cynicism in late-20th-century urban Scotland?"},
  {src:"ibo", subject:"Visual Arts", code:"visar", n:1, rq:"To what extent is Félix González-Torres's metaphorical use of found objects significant in conveying concepts of love and loss?"},
  {src:"ibo", subject:"Visual Arts", code:"visar", n:2, rq:"How has the Great Migration influenced Jacob Lawrence's visual narrative art collection The Migration Series?"},
  {src:"ibo", subject:"Visual Arts", code:"visar", n:3, rq:"In what ways did Japanese cultural art influence traditional French art between the 18th and 19th centuries?"},
  {src:"ibo", subject:"Chemistry", code:"chemi", n:1, rq:"What is the effect of temperature on the concentration of β-carotene extracted when orange peel powder is heated with ethanol under reflux for a retention time of 10 minutes?"},
  {src:"ibo", subject:"Chemistry", code:"chemi", n:2, rq:"How do variations in the concentration of hydrogen peroxide affect the intensity and the longevity of the light emitted by the chemiluminescent oxidation of luminol?"},
  {src:"ibo", subject:"Chemistry", code:"chemi", n:3, rq:"How will changing the temperature and time of the cold brewing process affect the tea polyphenol concentration in green tea water?"},
  {src:"ibo", subject:"Biology", code:"biolo", n:1, rq:"What is the effect of using different concentration masses of the Haloxylon salicornicum shrub in grams on catalase enzyme activity in cow, sheep and camel liver measured by the percentage of oxygen production using a vernier?"},
  {src:"ibo", subject:"Biology", code:"biolo", n:2, rq:"Are probiotics likely to be a viable treatment for major depressive disorder by influencing the microbiota–gut–brain axis?"},
  {src:"ibo", subject:"Biology", code:"biolo", n:3, rq:"To what extent does ocean acidification and reduction of pH affect coral Pocillopora damicornis and its resilience and decalcification rates?"},
  {src:"ibo", subject:"Physics", code:"physi", n:1, rq:"How is the angular speed of a rotating aluminium disk affected by the thickness of the disk and the magnitude of the magnetic field the disk is in?"},
  {src:"ibo", subject:"Physics", code:"physi", n:2, rq:"Investigating the effect of changing the space between the PC and SC and thickness of the iron core on the output power of the step-down transformer"},
  {src:"ibo", subject:"Physics", code:"physi", n:3, rq:"How does stationary contact time affect the coefficient of static friction in a tribosystem of two hard, planar surfaces producing dry friction?"},
  {src:"ibo", subject:"Economics", code:"econo", n:1, rq:"To what extent do the firms in the Singapore food delivery service engage in price and non-price competition?", marks:{A:3,B:3,C:3,D:3,E:2}, total:14, outOf:30},
  {src:"ibo", subject:"Economics", code:"econo", n:2, rq:"To what extent did the UK government's “Eat out to help out” scheme increase the consumption of restaurant food in Kent?"},
  {src:"ibo", subject:"Economics", code:"econo", n:3, rq:"How far has the “Beti bachao beti padhao” scheme introduced in 2015 been effective in lowering gender-based discrimination and raising gender equality in Barkhera area in Dhaulpur district, Rajasthan, India?"},
  {src:"ibo", subject:"Mathematics", code:"mathe", n:1, rq:"What are the fractal dimensions of the coastline of Antarctica?"},
  {src:"ibo", subject:"Mathematics", code:"mathe", n:2, rq:"How has the changing perception of infinity in set theory affected its associated paradoxes?"},
  {src:"ibo", subject:"Mathematics", code:"mathe", n:3, rq:"To what extent can the curve of fastest descent be used to model the efficiency of roofs in draining water?"},

  /* ── Previous-guide examples, rubric /34 (hosted by the IB) ── */
  {src:"old", subject:"Global Politics", code:"glopo", chapter:8, letterCode:"A", idx:1, rq:"What are the major hindrances in Tanzania and Pakistan to the achievement of human rights and how can they be tackled?", total:15, outOf:34},
  {src:"old", subject:"Global Politics", code:"glopo", chapter:8, letterCode:"B", idx:2, rq:"To what extent can Israel be fully democratic if its citizenship is based on ethnicity?", total:26, outOf:34},
  {src:"old", subject:"Global Politics", code:"glopo", chapter:8, letterCode:"C", idx:3, rq:"How far is Track II diplomacy a better approach to resolving interstate conflicts in the 21st century?", total:30, outOf:34},
  {src:"old", subject:"Business Management", code:"busman", chapter:4, letterCode:"A", idx:1, rq:"To what extent is it a good idea for Escan ltd to end a strategic alliance with Qupid?", total:19, outOf:34},
  {src:"old", subject:"Business Management", code:"busman", chapter:4, letterCode:"B", idx:2, rq:"To what extent is American Eagle Outfitters successful at using the extended marketing mix to influence consumer behaviour?", total:22, outOf:34}
];
