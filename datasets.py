dataset = [
     #Headache
    (["prevent headache", "headache prevent", "prevention for headache", "headache prevention"], "To prevent headaches, ensure you stay hydrated, maintain a healthy diet, get regular exercise, manage stress, and practice good posture. ", "z-img/biogesic.jpg", ["Ibuprofen", "Acetaminophen", "Biogesic"]),
    (["treat headache", "headache treat", "treatment for headache", "headache treatment"], "To treat a headache, you can try over-the-counter pain relievers like ibuprofen or biogesic, rest in a quiet and dark room, apply a cold compress to your forehead, and practice relaxation techniques such as deep breathing or meditation.", "z-img/biogesic.jpg", ["Ibuprofen", "Acetaminophen","Biogesic"]),

    (["burns prevent", "prevent burns", "prevention for burns", "burn prevention"], "Always use caution when handling hot objects or liquids. Keep hot objects out of reach of children. Install smoke alarms and have a fire extinguisher at home. Treat minor burns with cool running water and cover with a clean, dry cloth.", "z-img/prevent/prevent-burn.gif", []),
    (["burns treat", "treat burns", "treatment for burns", "burns treatment"], "For minor burns, run cool water over the affected area for at least 20 minutes. Do not apply ice. For severe burns, seek medical help immediately.",  "z-img/prevent/treat-burns.jpg", []),
    # Cuts and Wounds
    (["cut prevent", "prevent cut", "prevention for cut", "cut prevention"], "Handle sharp objects with care. Use appropriate safety gear, such as gloves and goggles, when working with sharp tools. Keep knives and other sharp objects out of reach of children. Clean cuts thoroughly with soap and water and apply an antibiotic ointment.", "z-img/prevent/prevent-cuts.png", ["Antibiotic ointment (Bacitracin)"]),
    (["cut treat", "treat cut", "treatment for cut", "cut treatment"], "Apply direct pressure to the wound to stop bleeding. Clean the wound with soap and water, and apply an antibiotic ointment. For deep cuts or wounds that won't stop bleeding, seek medical help.", "z-img/prevent/treat-cuts.png", ["Antibiotic ointment (Bacitracin)"]),
    # Sprains and Strains
    (["sprain prevent", "prevent sprain", "prevention for sprain", "sprain prevention"], "Warm up before exercising or engaging in physical activity. Wear appropriate footwear that provides support. Avoid uneven surfaces. Practice proper techniques when lifting heavy objects.", "z-img/prevent/prevent-sprains.png", []),
    (["sprain treat", "treat sprain", "treatment for sprain", "sprain treatment"], "Rest, ice, compress, and elevate (RICE) the affected area. Take over-the-counter pain medication if needed. Use crutches or a brace if necessary. If the pain or swelling is severe, seek medical help.", "z-img/prevent/treat-sprains.png", []),
    # Fractures
    (["fracture preven  t", "prevent fracture", "prevention for fracture", "fracture prevention"], "Wear appropriate protective gear when engaging in sports or activities that carry a risk of falls or collisions. Practice safety measures when driving or riding vehicles. Ensure your home is free of tripping hazards.", "z-img/prevent/prevent-fracture.png", []),
    (["fracture treat", "treat fracture", "treatment for fracture", "fracture treatment"], "Immobilize the affected area to prevent further injury. Apply ice to reduce swelling. Seek medical help immediately. Do not try to realign the bone yourself.", "z-img/prevent/treat-fracture.png", []),
    # Concussions
    (["concussion prevent", "prevent concussion", "prevention for concussion", "concussion prevention"], "Wear helmets during activities such as biking, skating, or playing contact sports. Avoid rough play and take precautions to prevent falls. Practice safe driving habits.", None, ["Ibuprofen (Advil)"]),  #none
    (["concussion treat", "treat concussion", "treatment for concussion", "concussion treatment"], "Rest and avoid activities that could worsen symptoms, such as physical or mental exertion. Seek medical help immediately if you suspect a concussion.", "z-img/prevent/treat-concussion.png", ["Ibuprofen (Advil)"]),
    # Bruises
    (["bruises prevent", "prevent bruises", "prevention for bruises", "bruise prevention"], "Take precautions to prevent falls. Use padding or cushions on sharp corners or edges. Avoid activities with a high risk of injury.", "z-img/prevent/prevent-bruse.jpg", ["Antibiotic Ointment (Bacitracin)"]),
    (["bruises treat", "treat bruises", "treatment for bruises", "bruises treatment"], "Apply a cold compress to reduce swelling. Elevate the affected area. If the bruise is accompanied by severe pain or swelling, seek medical help.", "z-img/prevent/treat-bruse.jpg", ["Antibiotic Ointment (Bacitracin)"]),
    # Nosebleeds
    (["nosebleed prevent", "prevent nosebleed", "prevention for nosebleed", "nosebleed prevention"], "Avoid picking your nose or blowing it too hard. Use a humidifier to keep the air moist. Apply a thin layer of petroleum jelly like Vaseline inside your nostrils.", "z-img/prevent/prevent-nosebleed.png", ["Vaseline Petroleum Jelly","Vicks Sinex"]),
    (["nosebleed treat", "treat nosebleed", "treatment for nosebleed", "nosebleed treatment"], "Lean forward slightly and pinch your nostrils together. Apply ice to the bridge of your nose. Seek medical help if the bleeding persists for more than 20 minutes.", "z-img/prevent/treat-nosebleed.jpg", ["Vaseline Petroleum Jelly", "Vicks Sinex"]),
    # Dislocations
    (["dislocation prevent", "prevent dislocation", "prevention for dislocation", "dislocation prevention"], "Warm up before physical activity. Strengthen muscles around joints with appropriate exercises. Use proper techniques when lifting heavy objects.", "z-img/prevent/prevent-dislocation.png", []),
    (["dislocation treat", "treat dislocation", "treatment for dislocation", "dislocation treatment"], "Do not try to realign the joint yourself. Immobilize the affected area and apply ice to reduce swelling. Seek medical help immediately.", "z-img/prevent/treat-dislocation.png", []),
    # Electric Shocks
    (["electric shock prevent", "prevent electric shock", "prevention for electric shock", "electric shock prevention"], "Unplug appliances before cleaning or repairing them. Keep electrical cords away from water. Use ground fault circuit interrupters (GFCIs) in areas where water is present.", "z-img/prevent/prevent-electric.jpg", []),
    (["electric shock treat", "treat electric shock", "treatment for electric shock", "electric shock treatment"], "Turn off the power source immediately. Do not touch the person until you are sure the power is off. If the person is unconscious, perform CPR if you are trained to do so. Seek medical help immediately.", "z-img/prevent/treat-electric.png", []),
    # Eye Injuries
    (["eye injuries prevent", "prevent eye injuries", "prevention for eye injuries", "eye injury prevention"], "Wear appropriate eye protection when working with hazardous materials or engaging in activities with a risk of eye injury. Avoid rubbing your eyes.", "z-img/prevent/prevent-eyes.jpg", []),
    (["eye injuries treat", "treat eye injuries", "treatment for eye injuries", "eye injuries treatment"], "Flush the eye with water for at least 15 minutes. Do not try to remove objects embedded in the eye. Seek medical help immediately.", "z-img/prevent/treat-eyes.png", []),
    # Poisoning
    (["poisoning prevent", "prevent poisoning", "prevention for poisoning", "poison prevention"], "Keep household chemicals and medications out of reach of children. Store them in their original containers with child-resistant caps. Never mix household chemicals. Practice food safety measures such as proper handwashing and cooking foods to the appropriate temperature. Refrigerate perishable foods promptly.", "z-img/prevent/prevent-poison.png", ["Cetaminophen", "Warfarin"]),
    (["poisoning treat", "treat poisoning", "treatment for poisoning", "poisoning treatment"], "If ingested, call Poison Control immediately. Follow their instructions. Do not induce vomiting unless instructed to do so. Seek medical help immediately.  ", None, ["Cetaminophen", "Warfarin"]), #none
    
    
    
    
    
    # Animal Bites
    (["animal bite prevent", "prevent animal bite", "prevention for animal bite", "animal bite prevention"], "Avoid approaching or disturbing animals, especially strays or wild animals. Do not provoke animals. Supervise children around animals.", None, ["Antibiotics", "Tetanus Vaccine", "Rabies Vaccine"]),   #none
    (["animal bite treat", "treat animal bite", "treatment for animal bite", "animal bite treatment"], "Wash the wound with soap and water. Apply an antibiotic ointment and cover with a clean bandage. Seek medical help, especially if the bite is deep or from a wild animal.", "z-img/prevent/treat-animal.png", []),
    # Heat Stroke
    (["heat stroke prevent", "prevent heat stroke", "prevention for heat stroke", "heat stroke prevention"], "Stay hydrated, especially in hot weather. Wear lightweight, loose-fitting clothing. Avoid strenuous activities during the hottest parts of the day.", "z-img/prevent/prevent-heat-stroke.jpg", []),
    (["heat stroke treat", "treat heat stroke", "treatment for heat stroke", "heat stroke treatment"], "Move to a cooler place and rest. Drink cool fluids if conscious. Apply cool compresses to the skin. Seek medical help immediately.", "z-img/prevent/treat-heat-stroke.png", []),
    # Hypothermia
    (["hypothermia prevent", "prevent hypothermia", "prevention for hypothermia", "hypothermia prevention"], "Dress warmly in layers when outdoors in cold weather. Stay dry and avoid prolonged exposure to cold temperatures. Seek shelter if necessary.", "z-img/prevent/prevent-hypothermia.jpg", ["Amiodarone (Cordarone)"]),
    (["hypothermia treat", "treat hypothermia", "treatment for hypothermia", "hypothermia treatment"], "Move to a warmer place and remove wet clothing. Wrap the person in blankets or warm clothing. Offer warm liquids if conscious. Seek medical help immediately.", "z-img/prevent/treat-hypothermia.png", ["Amiodarone (Cordarone)"]),
    # Choking
    (["choking prevent", "prevent choking", "prevention for choking", "choking prevention"], "Cut food into small pieces for young children. Supervise children while eating. Avoid giving small, round foods to young children.", "z-img/prevent/prevent-chocking.png", []),
    (["choking treat", "treat choking", "treatment for choking", "choking treatment"], "Perform the Heimlich maneuver if the person is conscious and choking. If the person is unconscious, perform CPR if trained to do so. Seek medical help immediately.", "z-img/prevent/treat-choke.png", []),
    # Drowning
    (["drowning prevent", "prevent drowning", "prevention for drowning", "drowning prevention"], "Supervise children around water at all times. Install pool fences and use life jackets when boating. Learn CPR.", "z-img/prevent/prevent-drowning.png", []),
    (["drowning treat", "treat drowning", "treatment for drowning", "drowning treatment"], "Remove the person from the water. Check for breathing and start CPR if necessary. Call emergency services immediately.", "z-img/prevent/treat-drowning.png", []),
    # Snake Bites
    (["snake bites prevent", "prevent snake bites", "prevention for snake bites", "snake bite prevention"], "Wear appropriate footwear and clothing when in areas where snakes may be present. Avoid provoking or handling snakes.", "z-img/prevent/prevent-snake.png", ["Antivenom"]),
    (["snake bites treat", "treat snake bites", "treatment for snake bites", "snake bites treatment"], "Keep the person calm and still. Remove jewelry or tight clothing from the affected area. Seek medical help immediately.", None, ["Antivenom"]),   #none
    # Frostbite
    (["frostbite prevent", "prevent frostbite", "prevention for frostbite", "frostbite prevention"], "Dress in layers and keep extremities covered in cold weather. Avoid prolonged exposure to cold temperatures and windy conditions. Keep skin dry.", "z-img/prevent/prevent-frost.png", []),
    (["frostbite treat", "treat frostbite", "treatment for frostbite", "frostbite treatment"], "Gradually warm the affected area with warm (not hot) water. Do not rub the area. Seek medical help immediately.", "z-img/prevent/treat-frost.jpg", []),
    # Asthma Attack
    (["asthma prevent", "prevent asthma", "prevention for asthma", "asthma prevention"], "Avoid triggers such as allergens, smoke, and pollution. Take prescribed medications regularly. Keep rescue inhaler on hand.", None, ["Bronchodilators", "Inhaled Corticosteroids (ICS)", "Leukotriene Modifiers"]), #none
    (["asthma treat", "treat asthma", "treatment for asthma", "asthma treatment"], "Use rescue inhaler as prescribed. Sit upright and remain calm. Seek medical help if symptoms do not improve or worsen.", "z-img/prevent/treat-asthma.png", ["Bronchodilators", "Inhaled Corticosteroids (ICS)", "Leukotriene Modifiers"]),   
    # Allergic Reaction
    (["allergic reaction prevent", "prevent allergic reaction", "prevention for allergic reaction", "allergic reaction prevention"], "Avoid known allergens. Carry an epinephrine auto-injector if prescribed. Wear a medical alert bracelet.", None, ["Antihistamines", "Decongestants"]),  #none
    (["allergic reaction treat", "treat allergic reaction", "treatment for allergic reaction", "allergic reaction treatment"], "Administer epinephrine auto-injector if available. Seek emergency medical help immediately.", "z-img/prevent/treat-allergy.png", ["Antihistamines", "Decongestants"]),
    # Heart Attack
    (["heart attack prevent", "prevent heart attack", "prevention for heart attack", "heart attack prevention"], "Maintain a healthy diet and weight. Exercise regularly. Manage stress. Avoid smoking and excessive alcohol consumption.", "z-img/prevent/prevent-heart.png", ["ACE Inhibitors", "Anticoagulants"]),
    (["heart attack treat", "treat heart attack", "treatment for heart attack", "heart attack treatment"], "Call emergency services immediately. Chew aspirin if not allergic. Keep person calm and comfortable until help arrives.", "z-img/prevent/treat-heart.png", ["ACE Inhibitors", "Anticoagulants"]),
    # Stroke
    (["stroke prevent", "prevent stroke", "prevention for stroke", "stroke prevention"], "Control high blood pressure, cholesterol, and diabetes. Exercise regularly. Maintain a healthy diet. Avoid smoking and excessive alcohol consumption.", "z-img/prevent/prevent-stroke.jpg", ["Emergency IV Medicine"]),
    (["stroke treat", "treat stroke", "treatment for stroke", "stroke treatment"], "Call emergency services immediately. Note the time when symptoms started. Keep person calm and monitor vital signs until help arrives.", "z-img/prevent/treat-stroke.png", ["Emergency IV medicine"]),
    # Severe Bleeding
    (["severe bleeding prevent", "prevent severe bleeding", "prevention for severe bleeding", "severe bleeding prevention"], "Handle sharp objects with care. Wear protective gloves when necessary. Keep first aid supplies readily available.", "z-img/prevent/prevent-cuts.png", ["Tranexamic Acid (Lysteda)"]),
    (["severe bleeding treat", "treat severe bleeding", "treatment for severe bleeding", "severe bleeding treatment"], "Apply direct pressure to the wound with a clean cloth. Elevate the wound above the heart if possible. Seek medical help immediately.", "z-img/prevent/treat-cuts.png", ["Tranexamic Acid (Lysteda)"]),
    # Seizure
    (["seizure prevent", "prevent seizure", "prevention for seizure", "seizure prevention"], "Take prescribed medications regularly. Get enough sleep. Avoid triggers such as stress, alcohol, and flashing lights.", None, ["Antiepileptic Drugs (AEDs)"]),  #none
    (["seizure treat", "treat seizure", "treatment for seizure", "seizure treatment"], "Keep the person safe from injury. Do not restrain them. Protect their head from injury. Stay with them until the seizure ends.", None, ["Antiepileptic Drugs (AEDs)"]),  #none
    # Fainting
    (["fainting prevent", "prevent fainting", "prevention for fainting", "fainting prevention"], "Avoid triggers such as standing for long periods, dehydration, and heat. Sit or lie down if feeling faint.", "z-img/prevent/prevent-fainting.png", ["Fludrocortisone Acetate"]),
    (["fainting treat", "treat fainting", "treatment for fainting", "fainting treatment"], "Lay the person flat on their back and raise their legs. Loosen tight clothing. Check for breathing and pulse. Seek medical help if necessary.", "z-img/prevent/treat-fainting.png", ["Fludrocortisone Acetate"]),
    # Heat Exhaustion
    (["heat exhaustion prevent", "prevent heat exhaustion", "prevention for heat exhaustion", "heat exhaustion prevention"], "Stay hydrated. Avoid strenuous activities in hot weather. Take breaks in shaded or air-conditioned areas.", "z-img/prevent/prevent-heatex.png", ["Benzodiazepines"]),
    (["heat exhaustion treat", "treat heat exhaustion", "treatment for heat exhaustion", "heat exhaustion treatment"], "Move to a cooler place. Remove excess clothing. Drink cool fluids. Apply cool compresses. Seek medical help if symptoms worsen or last longer than 1 hour.", "z-img/prevent/treat-heatex.png", ["Benzodiazepines"]),
  
   
    



    (["carbon monoxide poisoning prevent", "prevent carbon monoxide poisoning", "prevention for carbon monoxide poisoning", "carbon monoxide poisoning prevention"], "Install carbon monoxide detectors in your home. Ensure proper ventilation of gas appliances. Never use charcoal grills or generators indoors.", "z-img/prevent/prevent-carbon.jpg", []),
    (["carbon monoxide poisoning treat", "treat carbon monoxide poisoning", "treatment for carbon monoxide poisoning", "carbon monoxide poisoning treatment"], "Move to fresh air immediately. Seek medical help. Do not re-enter the area until it has been declared safe by authorities.", "z-img/prevent/treat-carbon.png", []),
    # Anaphylaxis
    (["anaphylaxis prevent", "prevent anaphylaxis", "prevention for anaphylaxis", "anaphylaxis prevention"], "Avoid known allergens. Carry an epinephrine auto-injector if prescribed. Wear a medical alert bracelet.", "z-img/prevent/treat-allergy.png", ["Epinephrine (Adrenaline)"]),
    (["anaphylaxis treat", "treat anaphylaxis", "treatment for anaphylaxis", "anaphylaxis treatment"], "Administer epinephrine auto-injector if available. Seek emergency medical help immediately.", "z-img/prevent/treat-allergy.png", ["Epinephrine (Adrenaline)"]),
    # Eye Irritation
    (["eye irritation prevent", "prevent eye irritation", "prevention for eye irritation", "eye irritation prevention"], "Avoid rubbing your eyes. Wear protective eyewear when necessary, such as when working with chemicals or participating in sports.", "z-img/prevent/prevent-eyes.jpg", ["Saline Eye Drops"]),
    (["eye irritation treat", "treat eye irritation", "treatment for eye irritation", "eye irritation treatment"], "Flush the eye with clean water for several minutes. Remove contact lenses if applicable. Seek medical help if irritation persists or worsens.", "z-img/prevent/treat-eyes.png", ["Saline Eye Drops"]),
    # Puncture Wounds
    (["puncture wounds prevent", "prevent puncture wounds", "prevention for puncture wounds", "puncture wounds prevention"], "Wear sturdy shoes when walking outdoors. Use caution when handling sharp objects or working with tools. Keep objects out of reach of children.", "z-img/prevent/prevent-puncture.jpg", ["Ointment (Neosporin)", "Polysporin"]),
    (["puncture wounds treat", "treat puncture wounds", "treatment for puncture wounds", "puncture wounds treatment"], "Clean the wound with soap and water. Apply an antibiotic ointment and cover with a sterile bandage. Seek medical help if the wound is deep or becomes infected.", "z-img/prevent/treat-puncture.png", ["Ointment (Neosporin)", "Polysporin"]),
    # Sunburn
    (["sunburn prevent", "prevent sunburn", "prevention for sunburn", "sunburn prevention"], "Apply sunscreen with a high SPF before going outdoors. Wear protective clothing, such as hats and sunglasses. Seek shade during peak sun hours.", "z-img/prevent/prevent-sunburn.jpg", ["Diphenhydramine", "Benadryl"]),
    (["sunburn treat", "treat sunburn", "treatment for sunburn", "sunburn treatment"], "Take a cool bath or apply cool compresses to the affected area. Moisturize with aloe vera or an unscented lotion. Take over-the-counter pain relievers if needed.", "z-img/prevent/treat-sunburn.png", ["Diphenhydramine", "Benadryl"]),
    # Dehydration
    (["dehydration prevent", "prevent dehydration", "prevention for dehydration", "dehydration prevention"], "Drink plenty of fluids throughout the day, especially in hot weather or during physical activity. Eat foods with high water content, such as fruits and vegetables.", "z-img/prevent/prevent-dehydration.png", ["Pedialyte","Drink Fluids"]),
    (["dehydration treat", "treat dehydration", "treatment for dehydration", "dehydration treatment"], "Drink water or oral rehydration solutions to replenish fluids. Rest in a cool, shaded area. Seek medical help if symptoms are severe or persistent.", "z-img/prevent/prevent-dehydration.png", ["Pedialyte","Drink Fluids"]),
    # Altitude Sickness
    (["altitude sickness prevent", "prevent altitude sickness", "prevention for altitude sickness", "altitude sickness prevention"], "Gradually ascend to higher altitudes to acclimatize. Stay hydrated. Avoid alcohol and strenuous exercise for the first few days at altitude.", "z-img/prevent/prevent-altitude.png", ["Acetazolamide (Diamox)"]),
    (["altitude sickness treat", "treat altitude sickness", "treatment for altitude sickness", "altitude sickness treatment"], "Descend to a lower altitude if symptoms are severe. Rest and drink plenty of fluids. Seek medical help if symptoms worsen or do not improve.", None, ["Acetazolamide (Diamox)"]), #none
    
    
    # Overexertion
    (["overexertion prevent", "prevent overexertion", "prevention for overexertion", "overexertion prevention"], "Gradually increase the intensity and duration of exercise. Take breaks as needed. Stay hydrated and maintain a balanced diet.", "z-img/prevent/prevent-overexertion.png", []),
    (["overexertion treat", "treat overexertion", "treatment for overexertion", "overexertion treatment"], "Rest and drink water or electrolyte-rich fluids. Apply ice packs to sore muscles. Seek medical help if symptoms are severe or persistent.", "z-img/prevent/treat-overexertion.png", []),
    # Road Rash
    (["road rash prevent", "prevent road rash", "prevention for road rash", "road rash prevention"], "Wear appropriate protective gear when cycling, skateboarding, or participating in other activities with a risk of falling. Avoid speeding and follow traffic laws.", "z-img/prevent/prevent-fracture.png", []),
    (["road rash treat", "treat road rash", "treatment for road rash", "road rash treatment"], "Clean the wound with soap and water. Apply an antibiotic ointment and cover with a sterile bandage. Seek medical help if the wound is deep or becomes infected.", "z-img/prevent/treat-fracture.png", []),
    # Sore Throat
    (["sore throat prevent", "prevent sore throat", "prevention for sore throat", "sore throat prevention"], "Practice good hygiene, such as washing hands frequently and avoiding close contact with sick individuals. Avoid smoking and exposure to secondhand smoke.", "z-img/prevent/prevent-sore.png", ["Antibacterial or antiseptic gargle", "Throat sprays"]),
    (["sore throat treat", "treat sore throat", "treatment for sore throat", "sore throat treatment"], "Rest and stay hydrated. Gargle with warm salt water. Use over-the-counter pain relievers or lozenges for relief. Seek medical help if symptoms persist or worsen.", "z-img/prevent/treat-sore.jpg", ["Antibacterial or antiseptic gargle", "Throat sprays"]),
    # Hangover
    (["hangover prevent", "prevent hangover", "prevention for hangover", "hangover prevention"], "Drink alcohol in moderation. Stay hydrated by drinking water between alcoholic beverages. Eat a meal before drinking.", "z-img/prevent/prevent-hangover.png", []),
    (["hangover treat", "treat hangover", "treatment for hangover", "hangover treatment"], "Stay hydrated with water or electrolyte-rich fluids. Eat a balanced meal. Get plenty of rest. Use over-the-counter pain relievers if needed.", "z-img/prevent/treat-hangover.jpg", []),
    # Indigestion
    (["indigestion prevent", "prevent indigestion", "prevention for indigestion", "indigestion prevention"], "Eat smaller, more frequent meals. Avoid trigger foods that cause indigestion, such as spicy or fatty foods. Eat slowly and chew food thoroughly.", "z-img/prevent/prevent-indigestion.png", ["Antacids", "H2 blockers", "Proton pump inhibitors (PPIs)"]),
    (["indigestion treat", "treat indigestion", "treatment for indigestion", "indigestion treatment"], "Take over-the-counter antacids or acid reducers. Drink water or herbal tea. Avoid lying down immediately after eating. Seek medical help if symptoms are severe or persistent.", "z-img/prevent/treat-indigestion.png", ["Antacids", "H2 blockers", "Proton pump inhibitors (PPIs)"]),
    # Motion Sickness
    (["motion sickness prevent", "prevent motion sickness", "prevention for motion sickness", "motion sickness prevention"], "Choose a seat where motion is felt the least, such as over the wings on an airplane or near the front in a car. Focus on the horizon or a stationary object.", None, ["Antihistamines", "Ginger"]), #none
    (["motion sickness treat", "treat motion sickness", "treatment for motion sickness", "motion sickness treatment"], "Rest and get fresh air. Drink ginger tea or take ginger supplements. Use over-the-counter medications such as dimenhydrinate or meclizine.", None, ["Antihistamines", "Ginger"]),  #none
    # Insomnia
    (["insomnia prevent", "prevent insomnia", "prevention for insomnia", "insomnia prevention"], "Maintain a regular sleep schedule. Create a relaxing bedtime routine. Avoid caffeine and electronic devices before bedtime.", "z-img/prevent/prevent-insomia.jpg", ["Melatonin", "Antihistamines", "Valerian"]),
    (["insomnia treat", "treat insomnia", "treatment for insomnia", "insomnia treatment"], "Create a comfortable sleep environment. Limit naps during the day. Practice relaxation techniques such as deep breathing or meditation. Seek medical help if insomnia persists.", "z-img/prevent/treat-insomia.png", ["Melatonin", "Antihistamines", "Valerian"]),
    
    
    
    
    # Acne
    (["acne prevent", "prevent acne", "prevention for acne", "acne prevention"], "Wash your face twice daily with a gentle cleanser. Avoid touching your face. Use non-comedogenic skincare products.", "z-img/prevent/prevent-acne.png", ["Benzoyl peroxide", "Azelaic acid"]),
    (["acne treat", "treat acne", "treatment for acne", "acne treatment"], "Use over-the-counter or prescription acne treatments as directed. Avoid picking or squeezing acne lesions. Follow a consistent skincare routine.", "z-img/prevent/treat-acne.png", ["Benzoyl peroxide", "Azelaic acid"]),
    # Migraine
    (["migraine prevent", "prevent migraine", "prevention for migraine", "migraine prevention"], "Identify and avoid triggers such as certain foods, stress, or lack of sleep. Maintain a regular sleep schedule. Stay hydrated.", "z-img/prevent/prevent-migraine.png", ["Ibuprofen", "Triptans", "Acetaminophen"]),
    (["migraine treat", "treat migraine", "treatment for migraine", "migraine treatment"], "Rest in a quiet, dark room. Apply a cold compress to the forehead. Take prescribed migraine medications as directed.", "z-img/prevent/treat-migraine.png", ["Ibuprofen", "Triptans", "Acetaminophen"]),
    # Back Pain
    (["back pain prevent", "prevent back pain", "prevention for back pain", "back pain prevention"], "Practice good posture. Lift heavy objects with your legs, not your back. Exercise regularly to strengthen back muscles.", "z-img/prevent/prevent-backpain.jpg", []),
    (["back pain treat", "treat back pain", "treatment for back pain", "back pain treatment"], "Apply heat or cold packs to the affected area. Take over-the-counter pain relievers as needed. Practice gentle stretching and exercise.", "z-img/prevent/treat-backpain.png", []),
    # Toothache
    (["toothache prevent", "prevent toothache", "prevention for toothache", "toothache prevention"], "Brush your teeth three times daily with fluoride toothpaste. Floss daily. Avoid sugary foods and drinks. Visit your dentist regularly for check-ups.", "z-img/prevent/prevent-tooth.png", ["Over-the-counter Pain Relievers"]),
    (["toothache treat", "treat toothache", "treatment for toothache", "toothache treatment"], "Rinse your mouth with warm salt water. Use over-the-counter pain relievers. Apply a cold compress to the cheek. See your dentist if pain persists.", "z-img/prevent/treat-tooth.jpg", ["Over-the-counter Pain Relievers"]),
    # Diarrhea
    (["diarrhea prevent", "prevent diarrhea", "prevention for diarrhea", "diarrhea prevention"], "Wash your hands frequently, especially before eating or preparing food. Drink clean, bottled water when traveling to areas with poor sanitation.", "z-img/prevent/prevent-diarrhea.png", ["Loperamide (Imodium)", "Antibiotics"]),
    (["diarrhea treat", "treat diarrhea", "treatment for diarrhea", "diarrhea treatment"], "Stay hydrated with clear fluids. Eat bland foods such as rice, bananas, and toast. Avoid dairy products and caffeine. Seek medical help if symptoms are severe or last longer than a few days.", "z-img/prevent/treat-diarrhea.jpg", ["Loperamide (Imodium)", "Antibiotics"]),
    # Constipation
    (["constipation prevent", "prevent constipation", "prevention for constipation", "constipation prevention"], "Eat a high-fiber diet rich in fruits, vegetables, and whole grains. Drink plenty of water. Exercise regularly.", "z-img/prevent/prevent-constipation.png", ["Stool softeners", "Amitiza"]),
    (["constipation treat", "treat constipation", "treatment for constipation", "constipation treatment"], "Increase fiber intake with foods or supplements. Stay hydrated. Exercise regularly. Use over-the-counter laxatives if needed.", "z-img/prevent/prevent-constipation.png", ["Stool softeners", "Amitiza"]), #same lang
    # Acid Reflux
    (["acid reflux prevent", "prevent acid reflux", "prevention for acid reflux", "acid reflux prevention"], "Avoid trigger foods such as spicy or fatty foods, caffeine, and citrus. Eat smaller, more frequent meals. Maintain a healthy weight.", "z-img/prevent/prevent-acidreflux.png", ["Antacids", "H2 Blockers", "Calcium carbonate (Alka-Seltzer)"]),
    (["acid reflux treat", "treat acid reflux", "treatment for acid reflux", "acid reflux treatment"], "Take over-the-counter antacids or acid reducers. Avoid lying down immediately after eating. Elevate the head of your bed. Avoid trigger foods.", "z-img/prevent/treat-acidreflux.png", ["Antacids", "H2 Blockers", "Calcium carbonate (Alka-Seltzer)"]),
    # Nausea
    (["nausea prevent", "prevent nausea", "prevention for nausea", "nausea prevention"], "Eat smaller, more frequent meals. Stay hydrated with clear fluids. Avoid strong odors and trigger foods.", None, ["Dimenhydrinate", "Ondansetron", "Diphenhydramine"]),  #none
    (["nausea treat", "treat nausea", "treatment for nausea", "nausea treatment"], "Rest in a quiet, dark room. Drink clear fluids such as water, ginger ale, or broth. Try over-the-counter medications such as bismuth subsalicylate or dimenhydrinate.", None, ["Dimenhydrinate", "Ondansetron", "Diphenhydramine"]),  #none
    # Acidosis
    (["acidosis prevent", "prevent acidosis", "prevention for acidosis", "acidosis prevention"], "Stay hydrated. Eat a balanced diet with plenty of fruits and vegetables. Avoid excessive alcohol consumption.", "z-img/prevent/prevent-acidosis.png", ["Sodium Citrate"]),
    (["acidosis treat", "treat acidosis", "treatment for acidosis", "acidosis treatment"], "Treat the underlying cause, such as diabetes or kidney disease. Restore the body's acid-base balance with medications or intravenous fluids. Seek medical help immediately.", "z-img/prevent/treat-acidosis.png", ["Sodium Citrate"]),
    
    
    
    
    
    
    
    
    
    # Alkalosis
    (["alkalosis prevent", "prevent alkalosis", "prevention for alkalosis", "alkalosis prevention"], "Stay hydrated. Avoid excessive vomiting or use of diuretics. Eat a balanced diet.", None, ["Ammonium Chloride"]),   #none
    (["alkalosis treat", "treat alkalosis", "treatment for alkalosis", "alkalosis treatment"], "Treat the underlying cause, such as dehydration or electrolyte imbalances. Restore the body's acid-base balance with medications or intravenous fluids. Seek medical help immediately.", None, ["Ammonium Chloride"]),  #none
    # Kidney Stones
    (["kidney stones prevent", "prevent kidney stones", "prevention for kidney stones", "kidney stones prevention"], "Stay hydrated by drinking plenty of water. Eat a balanced diet with adequate calcium and low oxalate levels. Limit sodium intake.", "z-img/prevent/prevent-kidney.png", ["Alpha Blockers", "Potassium Citrate"]),
    (["kidney stones treat", "treat kidney stones", "treatment for kidney stones", "kidney stones treatment"], "Drink plenty of water to help pass the stone. Use over-the-counter pain relievers. Seek medical help if symptoms are severe or if the stone does not pass.", "z-img/prevent/treat-kidneystones.png", ["Alpha Blockers", "Potassium Citrate"]),
    # Cystitis
    (["cystitis prevent", "prevent cystitis", "prevention for cystitis", "cystitis prevention"], "Stay hydrated. Urinate frequently, especially after sexual activity. Wipe from front to back after using the bathroom.", None, ["Trimethoprim-Sulfamethoxazole"]),   #none
    (["cystitis treat", "treat cystitis", "treatment for cystitis", "cystitis treatment"], "Drink plenty of water. Use over-the-counter pain relievers. Apply a heating pad to the abdomen. Seek medical help if symptoms persist or worsen.", None, ["Trimethoprim-Sulfamethoxazole"]),  #none
    # Prostatitis
    (["prostatitis prevent", "prevent prostatitis", "prevention for prostatitis", "prostatitis prevention"], "Practice safe sex. Urinate after sexual activity. Stay hydrated. Avoid prolonged sitting or bicycle riding.", "z-img/prevent/prevent-prostatitis.png", ["Doxycycline", "Trimethoprim-Sulfamethoxazole"]),
    (["prostatitis treat", "treat prostatitis", "treatment for prostatitis", "prostatitis treatment"], "Take prescribed antibiotics. Use over-the-counter pain relievers. Apply a heating pad to the pelvic area. Seek medical help if symptoms persist or worsen.", "z-img/prevent/treat-prostatitis.png", ["Doxycycline", "Trimethoprim-Sulfamethoxazole"]),
    # Urinary Tract Infection (UTI)
    (["UTI prevent", "prevent UTI", "prevention for UTI", "UTI prevention"], "To prevent urinary tract infections, stay hydrated by drinking plenty of water and maintain good hygiene practices, including wiping from front to back after using the bathroom. Additionally, empty your bladder regularly and urinate soon after sexual intercourse to flush out bacteria.", "z-img/prevent/prevent-uti.png", ["Fosfomycin", "Bactrim"]),  #SAME
    (["UTI treat", "treat UTI", "treatment for UTI", "UTI treatment"], "Urinary tract infections are typically treated with a course of antibiotics prescribed by a healthcare professional. It's important to complete the full course of medication to ensure the infection is fully eradicated and to follow any additional instructions provided by your doctor.", "z-img/prevent/prevent-uti.png", ["Fosfomycin", "Bactrim"]),
    # Laryngitis
    (["laryngitis prevent", "prevent laryngitis", "prevention for laryngitis", "laryngitis prevention"], "Avoid smoking and exposure to secondhand smoke. Stay hydrated. Avoid overusing your voice, especially in noisy environments.", "z-img/prevent/prevent-laryngitis.png", ["Corticosteroids", "Antibiotics"]),
    (["laryngitis treat", "treat laryngitis", "treatment for laryngitis", "laryngitis treatment"], "Rest your voice. Stay hydrated with warm liquids. Use a humidifier to add moisture to the air. Avoid irritants such as smoke or strong fumes.", "z-img/prevent/treat-laryngitis.png", ["Corticosteroids", "Antibiotics"]),
    # Strep Throat
    (["strep throat prevent", "prevent strep throat", "prevention for strep throat", "strep throat prevention"], "Practice good hygiene, such as washing hands frequently and avoiding close contact with sick individuals. Avoid sharing utensils or personal items.", "z-img/prevent/prevent-strep.png", ["Penicillin", "Amoxicillin"]),
    (["strep throat treat", "treat strep throat", "treatment for strep throat", "strep throat treatment"], "Take prescribed antibiotics. Get plenty of rest. Drink warm liquids such as tea or broth. Use over-the-counter pain relievers for relief.", "z-img/prevent/treat-strep.png", ["Penicillin", "Amoxicillin"]),
    # Tonsillitis
    (["tonsillitis prevent", "prevent tonsillitis", "prevention for tonsillitis", "tonsillitis prevention"], "To prevent tonsillitis, practicing good oral hygiene by regularly brushing teeth and using mouthwash can help reduce bacterial buildup. Avoiding exposure to cigarette smoke and other irritants can also lower the risk of developing tonsillitis.", "z-img/prevent/prevent-tonsil.png", ["Antibiotics", "Penicillin"]),
    (["tonsillitis treat", "treat tonsillitis", "treatment for tonsillitis", "tonsillitis treatment"], "Treatment for tonsillitis typically involves rest, staying hydrated, and over-the-counter pain relievers to manage symptoms. Antibiotics may be prescribed if the infection is bacterial, but viral cases usually resolve with supportive care.", None, ["Antibiotics", "Penicillin"]),  #none
    # Sinusitis
    (["sinusitis prevent", "prevent sinusitis", "prevention for sinusitis", "sinusitis prevention"], "To prevent sinusitis, maintain good nasal hygiene by using a saline nasal spray or rinse to keep nasal passages clear. Avoiding exposure to allergens and pollutants, and staying hydrated can also help prevent sinusitis.", None, ["Saline nasal spray"]), #none
    (["sinusitis treat", "treat sinusitis", "treatment for sinusitis", "sinusitis treatment"], "Treatment for sinusitis often involves nasal decongestants and saline nasal irrigation to alleviate congestion and promote sinus drainage. In cases of bacterial sinusitis, antibiotics may be prescribed, while over-the-counter pain relievers can help manage discomfort.", "z-img/prevent/treat-sinusitis.png", ["Saline nasal spray"]),
    
    
    
    
    
    # Pneumonia
    (["pneumonia prevent", "prevent pneumonia", "prevention for pneumonia", "pneumonia prevention"], "Get vaccinated against bacterial and viral infections such as flu and pneumococcus. Practice good hygiene, such as washing hands frequently. Avoid smoking and exposure to secondhand smoke.", "z-img/prevent/prevent-pneumonia.jpg", ["Amoxicillin", "Macrolides"]),
    (["pneumonia treat", "treat pneumonia", "treatment for pneumonia", "pneumonia treatment"], "Take prescribed antibiotics or antiviral medications. Get plenty of rest. Drink fluids to stay hydrated. Use over-the-counter pain relievers or fever reducers.", "z-img/prevent/treat-pnemonia.png", ["Amoxicillin", "Macrolides"]),
    # Pulmonary Embolism
    (["pulmonary embolism prevent", "prevent pulmonary embolism", "prevention for pulmonary embolism", "pulmonary embolism prevention"], "Move around during long periods of sitting, such as during travel or work. Stay hydrated. Use compression stockings if recommended.", "z-img/prevent/prevent-pulmonary.png", ["Heparin","Rivaroxaban"]),
    (["pulmonary embolism treat", "treat pulmonary embolism", "treatment for pulmonary embolism", "pulmonary embolism treatment"], "Seek emergency medical help immediately. Treatment may include blood thinners, clot-dissolving medications, or surgery.", None, ["Heparin","Rivaroxaban"]),  #none
    # Hypertension (High Blood Pressure)
    (["hypertension prevent", "prevent hypertension", "prevention for hypertension", "hypertension prevention"], "Prevent hypertension by maintaining a healthy weight through regular exercise and a balanced diet low in sodium and high in fruits and vegetables. Limiting alcohol intake and managing stress levels are also important measures in preventing hypertension.", "z-img/prevent/prevent-hypertension.png", ["Benazepril (Lotensin)", "Captopril (Capoten)"]),
    (["hypertension treat", "treat hypertension", "treatment for hypertension", "hypertension treatment"], "Hypertension treatment often involves lifestyle modifications such as adopting a low-sodium diet, regular exercise, and weight management. In addition, medication prescribed by a healthcare professional, such as ACE inhibitors or diuretics, may be necessary to lower blood pressure effectively.", "z-img/prevent/treat-hypertension.png", ["Benazepril (Lotensin)", "Captopril (Capoten)"]),
    # Hypotension (Low Blood Pressure)
    (["hypotension prevent", "prevent hypotension", "prevention for hypotension", "hypotension prevention"], "To prevent hypotension, ensure adequate hydration by drinking plenty of fluids and avoiding prolonged periods of standing. Incorporating small, frequent meals and gradually changing positions from lying to sitting or standing can also help prevent drops in blood pressure.", None, ["Midodrine (Orvaten)"]),  #none
    (["hypotension treat", "treat hypotension", "treatment for hypotension", "hypotension treatment"], "Treatment for hypotension may involve increasing salt intake, staying hydrated, and wearing compression stockings to improve blood flow. In severe cases, medication such as fludrocortisone or midodrine may be prescribed to raise blood pressure.", None, ["Midodrine (Orvaten)"]),   #none
    # Hyperglycemia (High Blood Sugar)
    (["hyperglycemia prevent", "prevent hyperglycemia", "prevention for hyperglycemia", "hyperglycemia prevention"], "Monitor blood sugar levels regularly. Follow a diabetes management plan including diet, exercise, and medication. Stay hydrated.", "z-img/prevent/prevent-hyperglycemia.png", ["Insulin"]),  
    (["hyperglycemia treat", "treat hyperglycemia", "treatment for hyperglycemia", "hyperglycemia treatment"], "Take prescribed diabetes medications or insulin as directed. Drink water to stay hydrated. Seek medical help if blood sugar levels are consistently high or if symptoms worsen.", "z-img/prevent/treat-hypoglycemia.png", ["Insulin"]),
    # Hypoglycemia (Low Blood Sugar)
    (["hypoglycemia prevent", "prevent hypoglycemia", "prevention for hypoglycemia", "hypoglycemia prevention"], "Eat regular meals and snacks. Monitor blood sugar levels regularly. Carry a fast-acting source of glucose such as glucose tablets or juice.", "z-img/prevent/prevent-hyperglycemia.png", ["Glucagon"]), #sameup
    (["hypoglycemia treat", "treat hypoglycemia", "treatment for hypoglycemia", "hypoglycemia treatment"], "Consume a fast-acting source of glucose such as glucose tablets, juice, or candy. Follow up with a snack or meal containing protein and carbohydrates. Seek medical help if symptoms do not improve.", "z-img/prevent/treat-hypoglycemia.png", ["Glucagon"]),
    # Hyperthermia (Heat Stroke)
    (["hyperthermia prevent", "prevent hyperthermia", "prevention for hyperthermia", "hyperthermia prevention"], "To prevent hyperthermia, stay hydrated by drinking plenty of water, especially in hot weather or during physical activity. Wear lightweight, breathable clothing, and avoid prolonged exposure to high temperatures by seeking shade or air-conditioned environments when necessary.", None, ["Benzodiazepines"]),  #none
    (["hyperthermia treat", "treat hyperthermia", "treatment for hyperthermia", "hyperthermia treatment"], "The treatment for hyperthermia involves cooling the body down rapidly, which can include moving to a cooler environment, removing excess clothing, and applying cool compresses or taking a cool bath. In severe cases, medical intervention such as intravenous fluids and other cooling measures may be necessary to lower body temperature quickly.", None, ["Benzodiazepines"]),  #none
    # Hypothermia
    (["hypothermia prevent", "prevent hypothermia", "prevention for hypothermia", "hypothermia prevention"], "To prevent hypothermia, dress warmly in layers, including moisture-wicking base layers, insulating materials, and a waterproof outer layer. Stay dry and avoid prolonged exposure to cold and wet conditions, and if outdoors in cold weather, be sure to stay hydrated and take breaks to warm up indoors periodically.", None, ["Amiodarone (Cordarone)"]),  #none
    (["hypothermia treat", "treat hypothermia", "treatment for hypothermia", "hypothermia treatment"], "The treatment for hypothermia involves gradually rewarming the body using passive measures such as blankets, warm clothing, and body-to-body contact, as well as active measures like warm fluids and heating pads applied to the trunk of the body. In severe cases, medical professionals may use more aggressive rewarming techniques such as warm intravenous fluids or extracorporeal rewarming methods.", None, ["Amiodarone (Cordarone)"]), #none
]    
    
   
   
   
symptom_dataset = [
    {
        "symptoms": ["fever", "high temperature"],
        "conditions": [
            {
                "condition": "Fever",
                "recommendation": "It seems like you might have a fever. Consider taking fever-reducing medication and staying hydrated.",
                "medications": ["Paracetamol", "Ibuprofen"]
            }
        ]
    },
    {
        "symptoms": ["sore throat", "throat pain"],
        "conditions": [
            {
                "condition": "Sore Throat",
                "recommendation": "It seems like you might have a sore throat. Drink warm liquids, use throat lozenges, and consider taking pain relief medication.",
                "medications": ["Throat Lozenges", "Paracetamol"]
            }
        ]
    },
    {
        "symptoms": ["runny nose", "nasal congestion"],
        "conditions": [
            {
                "condition": "Cold",
                "recommendation": "Based on your description, it seems like you might have a cold. Rest, drink plenty of fluids, and consider taking over-the-counter cold medication.",
                "medications": ["Over-the-counter cold medication"]
            }
        ]
    },
    {
        "symptoms": ["headache", "head pain"],
        "conditions": [
            {
                "condition": "Headache",
                "recommendation": "It seems like you might have a headache. Rest in a quiet, dark room and consider taking pain relief medication.",
                "medications": ["Paracetamol", "Ibuprofen"]
            }
        ]
    },
    {
        "symptoms": ["cough", "chest congestion"],
        "conditions": [
            {
                "condition": "Bronchitis",
                "recommendation": "You may have bronchitis. Consider taking cough suppressants, drinking plenty of fluids, and using a humidifier.",
                "medications": ["Cough suppressants", "Antibiotics (if bacterial infection)"]
            }
        ]
    },
    {
        "symptoms": ["shortness of breath", "difficulty breathing"],
        "conditions": [
            {
                "condition": "Asthma",
                "recommendation": "It seems like you might be experiencing asthma symptoms. Use your inhaler as prescribed and seek medical attention if symptoms worsen.",
                "medications": ["Inhaler (bronchodilator)", "Steroids"]
            }
        ]
    },
    {
        "symptoms": ["fatigue", "weakness"],
        "conditions": [
            {
                "condition": "Anemia",
                "recommendation": "You may be experiencing symptoms of anemia. Increase your iron intake through diet or supplements, and get plenty of rest.",
                "medications": ["Iron supplements", "Vitamin B12 supplements"]
            }
        ]
    },
    {
        "symptoms": ["stomach pain", "abdominal discomfort"],
        "conditions": [
            {
                "condition": "Gastritis",
                "recommendation": "It seems like you might have gastritis. Avoid spicy or acidic foods, eat smaller meals, and consider over-the-counter antacids.",
                "medications": ["Antacids", "Proton pump inhibitors"]
            }
        ]
    },
    {
        "symptoms": ["vomiting", "nausea"],
        "conditions": [
            {
                "condition": "Gastroenteritis",
                "recommendation": "Based on your symptoms, you may have gastroenteritis. Stay hydrated with clear fluids and avoid solid foods until symptoms subside.",
                "medications": ["Antiemetics", "Electrolyte solutions"]
            }
        ]
    },
    {
        "symptoms": ["diarrhea", "loose stools"],
        "conditions": [
            {
                "condition": "Diarrhea",
                "recommendation": "It seems like you might have diarrhea. Drink plenty of fluids to stay hydrated and consider over-the-counter medications to manage symptoms.",
                "medications": ["Antidiarrheal medication", "Oral rehydration salts"]
            }
        ]
    },
    {
        "symptoms": ["joint pain", "swelling"],
        "conditions": [
            {
                "condition": "Arthritis",
                "recommendation": "You may be experiencing symptoms of arthritis. Apply ice packs, rest the affected joint, and consider over-the-counter pain relievers.",
                "medications": ["Nonsteroidal anti-inflammatory drugs (NSAIDs)", "Corticosteroids"]
            }
        ]
    },
    {
        "symptoms": ["rash", "itchy skin"],
        "conditions": [
            {
                "condition": "Allergic Reaction",
                "recommendation": "Based on your symptoms, you may be having an allergic reaction. Avoid allergens if known, take antihistamines, and apply soothing lotions.",
                "medications": ["Antihistamines", "Topical corticosteroids"]
            }
        ]
    },
    {
        "symptoms": ["back pain", "lower back pain"],
        "conditions": [
            {
                "condition": "Muscle Strain",
                "recommendation": "It seems like you might have strained your back muscles. Apply ice packs, rest, and consider over-the-counter pain relievers.",
                "medications": ["Acetaminophen", "Nonsteroidal anti-inflammatory drugs (NSAIDs)"]
            }
        ]
    },
    {
        "symptoms": ["dizziness", "lightheadedness"],
        "conditions": [
            {
                "condition": "Vertigo",
                "recommendation": "Based on your symptoms, you may be experiencing vertigo. Avoid sudden movements, rest, and consult a healthcare professional.",
                "medications": ["Antihistamines", "Anti-nausea medications"]
            }
        ]
    },
    {
        "symptoms": ["difficulty swallowing", "painful swallowing"],
        "conditions": [
            {
                "condition": "Esophagitis",
                "recommendation": "You may have esophagitis. Avoid spicy or acidic foods, eat smaller meals, and consider over-the-counter antacids.",
                "medications": ["Antacids", "Proton pump inhibitors"]
            }
        ]
    },
    {
        "symptoms": ["frequent urination", "painful urination"],
        "conditions": [
            {
                "condition": "Urinary Tract Infection (UTI)",
                "recommendation": "It seems like you might have a urinary tract infection (UTI). Drink plenty of fluids, avoid irritants, and consider over-the-counter pain relievers.",
                "medications": ["Antibiotics", "Urinary analgesics"]
            }
        ]
    },
    {
        "symptoms": ["irregular heartbeat", "heart palpitations"],
        "conditions": [
            {
                "condition": "Arrhythmia",
                "recommendation": "You may be experiencing symptoms of arrhythmia. Avoid stimulants, get plenty of rest, and consult a healthcare professional for further evaluation.",
                "medications": ["Beta-blockers", "Calcium channel blockers"]
            }
        ]
    },
    {
        "symptoms": ["chest pain", "pressure in chest"],
        "conditions": [
            {
                "condition": "Heart Attack",
                "recommendation": "Based on your symptoms, you may be experiencing a heart attack. Call emergency services immediately and seek medical attention.",
                "medications": ["Aspirin", "Nitroglycerin"]
            }
        ]
    },
    {
        "symptoms": ["blood in stool", "rectal bleeding"],
        "conditions": [
            {
                "condition": "Hemorrhoids",
                "recommendation": "It seems like you might have hemorrhoids. Increase fiber intake, drink plenty of fluids, and consider over-the-counter hemorrhoid creams.",
                "medications": ["Hemorrhoid creams", "Stool softeners"]
            }
        ]
    },
    {
        "symptoms": ["muscle weakness", "fatigue"],
        "conditions": [
            {
                "condition": "Muscle Weakness",
                "recommendation": "You may be experiencing muscle weakness. Ensure adequate nutrition, rest, and consider physical therapy.",
                "medications": ["Vitamin supplements", "Calcium supplements"]
            }
        ]
    },
    {
        "symptoms": ["swollen lymph nodes", "tender lymph nodes"],
        "conditions": [
            {
                "condition": "Lymphadenitis",
                "recommendation": "Based on your symptoms, you may have lymphadenitis. Apply warm compresses, take over-the-counter pain relievers, and see a doctor if symptoms persist.",
                "medications": ["Pain relievers", "Antibiotics"]
            }
        ]
    },
    {
        "symptoms": ["memory loss", "confusion"],
        "conditions": [
            {
                "condition": "Dementia",
                "recommendation": "It seems like you might be experiencing symptoms of dementia. Consult a healthcare professional for evaluation and management.",
                "medications": ["Cholinesterase inhibitors", "Memantine"]
            }
        ]
    },
    {
        "symptoms": ["seizures", "convulsions"],
        "conditions": [
            {
                "condition": "Epilepsy",
                "recommendation": "You may be experiencing seizures due to epilepsy. Follow your prescribed seizure management plan and seek medical advice.",
                "medications": ["Antiepileptic drugs", "Benzodiazepines"]
            }
        ]
    },
    {
        "symptoms": ["vision changes", "blurred vision"],
        "conditions": [
            {
                "condition": "Vision Impairment",
                "recommendation": "It seems like you might have vision impairment. Schedule an eye examination with an optometrist or ophthalmologist for evaluation.",
                "medications": ["Eyeglasses", "Contact lenses"]
            }
        ]
    },
    {
        "symptoms": ["hair loss", "bald patches"],
        "conditions": [
            {
                "condition": "Alopecia",
                "recommendation": "Based on your symptoms, you may have alopecia. Consult a dermatologist for evaluation and management options.",
                "medications": ["Minoxidil", "Corticosteroid injections"]
            }
        ]
    },
    {
        "symptoms": ["unexplained weight loss", "loss of appetite"],
        "conditions": [
            {
                "condition": "Malnutrition",
                "recommendation": "It seems like you might be experiencing malnutrition. Ensure a balanced diet with adequate calorie intake and consider nutritional supplements.",
                "medications": ["Multivitamins", "Nutritional supplements"]
            }
        ]
    },
    {
        "symptoms": ["excessive thirst", "frequent urination"],
        "conditions": [
            {
                "condition": "Diabetes",
                "recommendation": "You may have diabetes. Monitor blood sugar levels, follow a diabetic diet, and consult a healthcare professional for management.",
                "medications": ["Insulin", "Oral antidiabetic drugs"]
            }
        ]
    },
    {
        "symptoms": ["mood swings", "irritability"],
        "conditions": [
            {
                "condition": "Mood Disorders",
                "recommendation": "Based on your symptoms, you may have a mood disorder. Seek counseling or psychiatric evaluation for diagnosis and management.",
                "medications": ["Antidepressants", "Mood stabilizers"]
            }
        ]
    },
    {
        "symptoms": ["frequent headaches", "migraine attacks"],
        "conditions": [
            {
                "condition": "Migraine",
                "recommendation": "It seems like you might be experiencing migraines. Identify triggers, manage stress, and consider preventive medications.",
                "medications": ["Triptans", "Beta-blockers"]
            }
        ]
    },
    {
        "symptoms": ["excessive sweating", "night sweats"],
        "conditions": [
            {
                "condition": "Hyperhidrosis",
                "recommendation": "You may have hyperhidrosis. Use antiperspirants, wear breathable clothing, and consult a dermatologist for treatment options.",
                "medications": ["Antiperspirants", "Iontophoresis"]
            }
        ]
    },
    {
        "symptoms": ["excessive hunger", "weight gain"],
        "conditions": [
            {
                "condition": "Hypothyroidism",
                "recommendation": "Based on your symptoms, you may have hypothyroidism. Get thyroid function tests done and consult an endocrinologist for management.",
                "medications": ["Levothyroxine", "Liothyronine"]
            }
        ]
    }
]


symptom_dataset += [
    {
        "symptoms": ["severe abdominal pain", "bloody stool"],
        "conditions": [
            {
                "condition": "Crohn's Disease",
                "recommendation": "It seems like you might have Crohn's disease. Follow a low-fiber diet, take anti-inflammatory medications, and consult a gastroenterologist for management.",
                "medications": ["Corticosteroids", "Immunomodulators"]
            }
        ]
    },
    {
        "symptoms": ["excessive thirst", "frequent urination"],
        "conditions": [
            {
                "condition": "Diabetes Mellitus",
                "recommendation": "Based on your symptoms, you may have diabetes mellitus. Monitor blood sugar levels, follow a balanced diet, and take insulin or oral medications as prescribed.",
                "medications": ["Insulin", "Metformin"]
            }
        ]
    },
    {
        "symptoms": ["sudden chest pain", "shortness of breath"],
        "conditions": [
            {
                "condition": "Myocardial Infarction (Heart Attack)",
                "recommendation": "It seems like you might be experiencing a heart attack. Call emergency services immediately, chew aspirin if available, and wait for medical assistance.",
                "medications": ["Aspirin", "Thrombolytics"]
            }
        ]
    },
    {
        "symptoms": ["difficulty speaking", "facial drooping"],
        "conditions": [
            {
                "condition": "Stroke",
                "recommendation": "Based on your symptoms, you may be having a stroke. Call emergency services immediately and note the time of symptom onset for timely treatment.",
                "medications": ["Tissue plasminogen activator (tPA)", "Antiplatelet drugs"]
            }
        ]
    },
    {
        "symptoms": ["swelling in legs", "shortness of breath"],
        "conditions": [
            {
                "condition": "Pulmonary Embolism",
                "recommendation": "It seems like you might have a pulmonary embolism. Seek immediate medical attention, keep calm, and avoid physical exertion.",
                "medications": ["Anticoagulants", "Thrombolytics"]
            }
        ]
    },
    {
        "symptoms": ["confusion", "hallucinations"],
        "conditions": [
            {
                "condition": "Delirium",
                "recommendation": "Based on your symptoms, you may have delirium. Ensure a calm environment, address underlying causes, and seek medical evaluation.",
                "medications": ["Antipsychotics", "Sedatives"]
            }
        ]
    },
    {
        "symptoms": ["painful urination", "lower abdominal pain"],
        "conditions": [
            {
                "condition": "Bladder Infection",
                "recommendation": "It seems like you might have a bladder infection. Drink plenty of water, use antibiotics as prescribed, and avoid irritants like caffeine.",
                "medications": ["Antibiotics", "Urinary analgesics"]
            }
        ]
    },
    {
        "symptoms": ["weight loss", "fatigue"],
        "conditions": [
            {
                "condition": "Hyperthyroidism",
                "recommendation": "You may have hyperthyroidism. Follow up with an endocrinologist, take antithyroid medications, and consider radioactive iodine therapy or surgery.",
                "medications": ["Antithyroid medications", "Beta blockers"]
            }
        ]
    },
    {
        "symptoms": ["difficulty sleeping", "daytime sleepiness"],
        "conditions": [
            {
                "condition": "Sleep Apnea",
                "recommendation": "Based on your symptoms, you may have sleep apnea. Use a CPAP machine, maintain a healthy weight, and avoid alcohol and sedatives.",
                "medications": ["Continuous positive airway pressure (CPAP)", "Oral appliances"]
            }
        ]
    },
    {
        "symptoms": ["blood in urine", "pain in the side or back"],
        "conditions": [
            {
                "condition": "Kidney Stones",
                "recommendation": "It seems like you might have kidney stones. Stay hydrated, manage pain with NSAIDs, and consult a urologist for further evaluation and treatment.",
                "medications": ["NSAIDs", "Alpha blockers"]
            }
        ]
    },
    {
        "symptoms": ["persistent cough", "chest pain"],
        "conditions": [
            {
                "condition": "Pneumonia",
                "recommendation": "Based on your symptoms, you may have pneumonia. Rest, stay hydrated, and use antibiotics as prescribed by a healthcare provider.",
                "medications": ["Antibiotics", "Antipyretics"]
            }
        ]
    },
    {
        "symptoms": ["mood swings", "loss of interest"],
        "conditions": [
            {
                "condition": "Depression",
                "recommendation": "It seems like you might have depression. Seek therapy, consider antidepressant medications, and maintain a support network.",
                "medications": ["Selective serotonin reuptake inhibitors (SSRIs)", "Serotonin-norepinephrine reuptake inhibitors (SNRIs)"]
            }
        ]
    },
    {
        "symptoms": ["difficulty swallowing", "unexplained weight loss"],
        "conditions": [
            {
                "condition": "Esophageal Cancer",
                "recommendation": "You may have esophageal cancer. Consult an oncologist for diagnosis and treatment options, which may include surgery, chemotherapy, and radiation therapy.",
                "medications": ["Chemotherapy", "Targeted therapy"]
            }
        ]
    },
    {
        "symptoms": ["pain in the lower abdomen", "irregular menstruation"],
        "conditions": [
            {
                "condition": "Polycystic Ovary Syndrome (PCOS)",
                "recommendation": "Based on your symptoms, you may have PCOS. Manage symptoms with lifestyle changes, hormonal contraceptives, and metformin.",
                "medications": ["Oral contraceptives", "Metformin"]
            }
        ]
    },
    {
        "symptoms": ["memory loss", "difficulty finding words"],
        "conditions": [
            {
                "condition": "Alzheimer's Disease",
                "recommendation": "It seems like you might have Alzheimer's disease. Consult a neurologist for evaluation, consider cognitive enhancers, and plan for long-term care.",
                "medications": ["Cholinesterase inhibitors", "Memantine"]
            }
        ]
    }
]