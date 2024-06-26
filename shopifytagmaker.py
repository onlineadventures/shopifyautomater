import csv
import anthropic

# Set up Anthropic API key
anthropic_api_key = "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"
anthropic.api_key = anthropic_api_key

# Function to generate tags using Claude AI
def generate_tags(title, body, option1_value):
    # Hard-coded list of potential tags
    possible_tags = "Fireclay, Refractory Mortar, Hunter Fullers, Roadster Fullers, Ridolo Fullers, Top Fullers, Handheld Top Fullers, Power Hammer Top Fullers, Bottom Fullers, Bottom Fullers, Anvil Mounted Bottom Fullers, Swage Block Bottom Fullers, Fuller Sets, Matching Top and Bottom Fuller Sets, Assorted Fuller Collections, Punches, Slot Punches, Narrow Slot Punches, Wide Slot Punches, Round Punches, Round Punches, Small Diameter Round Punches, Large Diameter Round Punches, Square Punches, Square Punches, Small Square Punches, Large Square Punches, Drift Punches, Tapered Drift Punches, Parallel Drift Punches, Specialty Tools, Swages, Top Swage, Bottom Swage, Swage Block, Bowl Swages, Spoon Swages, Veining Chisels, Narrow Veining Chisels, Wide Veining Chisels, Hot Cutters, Handheld Hot Cutters, Hardy Hole Hot Cutters, Cold Cutters, Handheld Cold Cutters, Bench Cold Cutters, Tool Sets, Beginner Sets, Chisel Set, Punch Sets, Starter Fuller Sets, Professional Sets, Comprehensive Chisel Sets, Full Range Punch Sets, Complete Fuller and Swage Sets, Tool Accessories, Handles and Grips, Replacement Wooden Handles, Rubber Grip Sleeves, Tool Racks and Holders, Wall Mounted Tool Racks, Benchtop Tool Stands, Maintenance and Repair, Sharpening Tools, Whetstones, Honing Rods, Maintenance Kits, Chisel Care Kits, Punch Preservation Kits, Safety Equipment, Hand Protection, Leather Gloves, Impact-Resistant Gloves, Eye Protection, Safety Glasses, Face Shields, Swage Blocks, Cast Iron Swage Blocks, Standard Cast Iron Swage Blocks, Custom Design Cast Iron Swage Blocks, Steel Swage Blocks, Heavy-Duty Steel Swage Blocks, Portable Steel Swage Blocks, Swage Block Accessories, Swage Block Stands, Swage Block Covers, Mandrels, Horn Mandrels, Anvil Horn Mandrels, Standalone Horn Mandrels, Cone Mandrels, Floor Cone Mandrels, Benchtop Cone Mandrels, Stake Mandrels, T Stake Mandrels, Yoke Stake Mandrels, Ring Mandrels, Solid Ring Mandrels, Adjustable Ring Mandrels, Specialty Mandrels, Dishing Mandrels, Dishing Form Mandrels, Dishing Block Mandrels, Plate Mandrels, Flat Plate Mandrels, Shaped Plate Mandrels, Tube Mandrels, Solid Tube Mandrels, Hollow Tube Mandrels, Swage Block and Mandrel Sets, Beginner Sets, Basic Swage Block and Mandrel Sets, Introductory Shaping Sets, Professional Sets, Comprehensive Swage Block Sets, Advanced Mandrel Collections, Maintenance and Repair, Care Kits, Swage Block Maintenance Kits, Mandrel Preservation Kits, Replacement Parts, Mandrel Pins and Caps, Swage Block Inserts, Tool Stands and Racks, Swage Block Stands, Heavy-Duty Stands, Adjustable Stands, Mandrel Racks, Wall Mounted Racks, Freestanding Racks, Safety Equipment, Protective Gear, Hand Protection Gloves, Heavy-Duty Aprons, Tool Guards, Edge Protectors, Surface Covers, Abrasive Tools, Grinding Wheels, Bench Grinder Wheels, Angle Grinder Discs, Sanding Belts, Narrow Belts for Detail Work, Wide Belts for Surface Finishing, Sanding Discs, Hook and Loop Sanding Discs, Adhesive-Backed Sanding Discs, Flap Wheels, Mounted Flap Wheels, Flap Discs for Angle Grinders, Polishing Tools, Polishing Wheels, Cotton Polishing Wheels, Felt Polishing Wheels, Polishing Compounds, Metal Polishing Compounds, Buffing Compounds, Buffing Pads, Foam Buffing Pads, Wool Buffing Pads, Hand Finishing Tools, Files and Rasps, Metal Files, Wood Rasps, Burnishing Tools, Steel Burnishers, Agate Burnishers, Wire Brushes, Hand Wire Brushes, Drill-Mounted Wire Brushes, Specialty Finishing Tools, Etching Tools, Electrochemical Etching Machines, Etching Stencils and Solutions, Patina Solutions, Copper Patina Solutions, Steel Patina Solutions, Engraving Tools, Hand Engraving Tools, Power Engraving Tools, Finishing Kits, Starter Kits, Basic Polishing Kits, Basic Finishing Kits, Professional Kits, Deluxe Polishing Kits, Comprehensive Finishing Kits, Surface Treatment Supplies, Clear Coats, Spray-On Clear Coats, Brush-On Clear Coats, Rust Preventatives, Rust Inhibitor Sprays, Rust Preventative Oils, Sealants, Sealant Gun, Metal Sealants, Wood Sealants, Cleaning and Maintenance, Cleaning Solutions, Metal Cleaning Solutions, Degreasing Solutions, Maintenance Tools, Polishing Tool Cleaners, Abrasive Cleaners, Safety Equipment, Protective Eyewear, Safety Glasses, Face Shields, Hand Protection, Work Gloves, Vibration-Dampening Gloves, Quenching Oils, Fast Quenching Oils, Cutting Oil, Accelerated Cooling Oils, High-Speed Steels Quenching Oils, Medium Quenching Oils, General Purpose Quenching Oils, Medium Speed Quenching Oils, Slow Quenching Oils, Low-Speed Quenching Oils, Oil for Delicate or Intricate Pieces, Water-Based Quenchants, Polymer Quenchants, High Concentration Polymer Quenchants, Low Concentration Polymer Quenchants, Water-Soluble Oils, Emulsifiable Oils, Synthetic Water-Based Quenchants, Specialty Quenching Fluids, Hot Quenching Oils, Oils for High-Temperature Quenching, Pre-Heated Quenching Oils, Cold Quenching Solutions, Brine Solutions, Cryogenic Quenching Agents, Quenching Additives, Anti-Oxidation Additives, Rust Inhibitors, Oxidation Preventives, Cooling Enhancers, Accelerators for Quenching Speed, Temperature Stabilizers, Quenching Systems and Equipment, Quenching Tanks, Steel Quenching Tanks, Insulated Quenching Tanks, Agitation Systems, Mechanical Agitators, Pneumatic Agitation Systems, Temperature Control Systems, Quench Oil Heaters, Cooling Systems for Quenchants, Maintenance and Safety Supplies, Quenchant Testing Kits, Oil Quality Test Kits, Water-Based Quenchant Test Kits, Spill Response Kits, Oil Spill Kits, Chemical Spill Kits, Safety Equipment, Chemical Resistant Gloves, Safety Goggles and Face Shields, Storage and Handling, Storage Containers, Steel Drums for Oil Storage, Chemical Storage Tanks, Transfer Pumps and Funnels, Manual Transfer Pumps, Electric Drum Pumps, Waste Disposal Solutions, Oil Recycling Containers, Hazardous Waste Disposal Kits, Forge Construction Components, Forge Bodies, Gas Forge Shells, Coal Forge Pans, Forge Liners and Insulation, Ceramic Fiber Blankets, Refractory Cement and Coatings, Forge Floors, Firebrick, Castable Refractory Floors, Heating and Fuel Components, Burners, Propane Burners, Natural Gas Burners, Blowers and Fans, Electric Blowers, Hand Crank Blowers, Fuel Lines and Regulators, Gas Hoses, Pressure Regulators, Airflow and Ventilation, Flues and Chimneys, Metal Chimney Pipes, Chimney Caps, Air Gates and Tuyeres, Sliding Air Gates, Rotary Tuyeres, Exhaust Systems, Forge Hoods, Ventilation Fans, Forge Tools and Accessories, Fire Tools, Fire Pokers, Coal Rakes, Work Supports, Anvil Stands, Tool Racks, Forge Covers, Insulating Covers, Weatherproof Covers, Temperature Measurement and Control, Thermocouples and Pyrometers, Digital Pyrometers, Analog Thermocouples, Temperature Controllers, PID Controllers, Thermostatic Controllers, Maintenance and Repair Supplies, Replacement Parts, Replacement Burners, Spare Blower Parts, Cleaning Tools, Forge Brushes, Slag Hammers, Repair Kits, Refractory Patch Kits, Burner Maintenance Kits, Safety Equipment, Protective Gear, Heat Resistant Gloves, Forge Aprons, Fire Safety, Fire Extinguishers, Fire Blankets, Customization and Upgrades, Custom Forge Doors, Sliding Doors, Swing Doors, Enhanced Burners, High-Efficiency Burners, Multi-Fuel Burners, Decorative Elements, Forge with Hoods, Decorative Ironwork, Material Types, Leather Aprons, Full-Grain Leather Aprons, Split Leather Aprons, Canvas Aprons, Heavy-Duty Canvas Aprons, Waxed Canvas Aprons, Synthetic Aprons, Fire-Resistant Synthetic Aprons, Water-Resistant Synthetic Aprons, Style and Design, Full-Length Aprons, Bib Aprons with Full Coverage, Floor-Length Aprons for Extra Protection, Waist Aprons, Short Waist Aprons, Long Waist Aprons with Extended Coverage, Specialty Aprons, Farrier Aprons with Leg Protection, Welder's Leather Aprons with Heat Resistance, Features, Pockets and Storage, Aprons with Tool Pockets, Aprons with Utility Loops and Clips, Adjustable Straps, Cross-Back Strap Aprons, Neck Strap Aprons with Buckle Adjustments, Reinforced Stitching and Rivets, Riveted Stress Points for Durability, Double-Stitched Seams for Longevity, Customization Options, Custom Sizes, Made-to-Measure Aprons for Perfect Fit, Plus-Size and Petite Options, Personalization, Monogramming Services, Custom Logo Embossing, Accessories and Add-Ons, Protective Sleeves, Leather Arm Guards, Heat-Resistant Sleeves, Apron Care Kits, Leather Conditioning Creams, Canvas Waterproofing Waxes, Safety Features, Heat Resistance, Aprons with Heat-Resistant Linings, Aluminized Aprons for High-Temperature Work, Spark and Splatter Protection, Aprons with Fire-Resistant Coatings, Aprons with Kevlar Thread Stitching, Decorative Hinges, Strap Hinges, Hand-Forged Iron Strap Hinges, Decorative Brass Strap Hinges, Butt Hinges, Ornamental Cast Butt Hinges, Decorative Leaf Butt Hinges, Pintle Hinges, Rustic Pintle Hinges, Decorative Gudgeon and Pintle Hinges, Latches and Locks, Thumb Latches, Traditional Blacksmith Thumb Latches, Victorian Style Thumb Latches, Bolt Latches, Slide Bolt Latches, Barrel Bolt Latches, Decorative Locks, Antique Replica Locks, Ornate Padlocks and Hasps, Handles and Pulls, Door Handles and Pulls, Wrought Iron Door Handles, Cast Bronze Door Pulls, Drawer Handles and Pulls, Decorative Drawer Handles, Hand-Crafted Drawer Pulls, Cabinet Handles and Pulls, Forged Cabinet Handles, Artisan Crafted Cabinet Pulls, Knobs and Hooks, Decorative Knobs, Hand-Forged Knobs, Ceramic and Glass Knobs, Wall Hooks, Wrought Iron Wall Hooks, Decorative Coat and Hat Hooks, Fasteners and Connectors, Decorative Nails and Studs, Hand-Forged Nails, Double Studs, Decorative Upholstery Tacks, Brackets and Braces, Ornamental Shelf Brackets, Decorative Corner Braces, Clavos and Rosettes, Decorative Door Studs, Hand-Hammered Rosettes, Specialty Hardware, Window Hardware, Decorative Window Latches, Ornamental Shutter Dogs, Furniture Hardware, Decorative Furniture Locks, Artistic Furniture Connectors, Barn Door Hardware, Rustic Barn Door Track Systems, Hand-Forged Barn Door Rollers, Restoration and Antique Hardware, Historical Replicas, Period-Accurate Hardware Replicas, Restoration Hardware for Antiques, Patina and Finishes, Aged Bronze Finishes, Distressed Iron Patinas, Customization Options, Custom Design Services, Bespoke Hardware Designs, Personalized Engraving and Embossing, Installation and Maintenance, Installation Kits, Hardware Mounting Kits, Alignment and Measurement Tools, Care and Preservation, Metal Polish and Wax, Protective Coatings and Sealants, Fasteners & Connectors, Anvils & Stands, Measuring & Layout Tools, Material Stock (Metals & Alloys), Forging Hammers, Tongs & Pliers, Heating Equipment, Power Hammers & Presses, Grinders & Sanders, Chisels, Fullers & Punches, Hardy Tools, Swage Blocks & Mandrels, Finishing & Polishing Tools, Quenching Oils & Fluids, Forges and Burners, Forging Kits, Forge Parts & Accessories, Blacksmithing Aprons, Decorative Hardware & Fasteners,6 Head and Face Protection, Safety Goggles and Glasses, Full Face Shields / Face Visor, Welding Helmets, Heat-Resistant Face Masks, Protective Headbands and Caps, Hearing Protection, Noise-Canceling Ear Muffs, Ear Plugs, High Fidelity Ear Protectors for Forge Work / Ear Defenders, Hand and Arm Protection, Leather Forge Gloves, Cut-Resistant Gloves, Arm Guards and Sleeves, Vibration-Dampening Gloves, High-Temperature Welding Gloves, Aluminised Oversleeves, Water-Proof Latex Gloves, Welders Oversleeves, Body Protection, Leather Aprons, Fire-Resistant Coveralls, Heat-Resistant Shop Coats, Spatter-Proof Clothing / Oversleeves, Worker Jacket, Welding Jackets and Vests, Bib Apron, Foot Protection, Steel-Toed Boots, Metatarsal Guards, Heat-Resistant Shoe Covers, Slip-Resistant Work Shoes, Electric Hazard Safety Shoes, Respiratory Protection, Dust Masks, Half-Mask Respirators, Full-Face Respirator Masks, Powered Air Purifying Respirators, Disposable Respirators for Particulates, Skin Protection, Barrier Creams and Lotions, Heat and Burn Creams, UV Protection Lotions for Welders, Hydration and Repair Hand Creams, High-Visibility Gear, Reflective Safety Vests, High-Visibility Shirts and Jackets, LED Safety Bands and Lights, Glow in the Dark Tape and Markings, Cooling Gear, Cooling Vests and Jackets, Neck Cooling Wraps, Cooling Bandanas and Headbands, Hydration Packs with Cooling Technology, Supportive Gear, Back Support Belts, Knee Pads and Cushions, Anti-Fatigue Floor Mats, Wrist Support and Compression Gloves, Emergency and First Aid, Burn Kits and Gels, First Aid Kits for Workshops, Eye Wash Stations, Fire Extinguishers and Blankets, Emergency Escape Masks, Rulers and Measuring Tapes, Steel Ruler, Fiberglass Tape Measure, Hook Rulers for Precision, Folding Rulers, Digital Measuring Wheel, Calipers and Micrometers, Calipers, Digital Calipers, Inside and Outside Micrometers, Dial Calipers, Depth Micrometers, Squares and Angles, Try Squares, Framing Squares, Sliding Bevels, Angle Finders, Combination Squares, Levels and Plumb Bobs, Spirit Levels Various Sizes, Tripod Laser Levels, Torpedo Levels, Plumb Bobs, Line Levels, Marking Tools, Soapstone Markers, Metal Scribing Tools, Chalk Line Reels, Punches for Marking, Marking Gauges, Protractors and Compasses, Digital Protractors, Angle Protractors, Wing and Traditional Compasses, Dividers for Precision Layout, Radius Markers, Feeler and Thickness Gauges, Feeler Gauge Sets, Wire and Sheet Metal Thickness Gauges, Dial Thickness Gauges, Digital Thickness Gauges, Height and Depth Gauges, Vernier Height Gauges, Dial Depth Gauges, Digital Height Gauges, Depth Base Attachments, Templates and Stencils, Curve Templates, Letter and Number Stencils, Welding and Cutting Templates, French Curves, Precision Straight Edges, Inspection Straight Edges, Machinist's Straight Edges, Precision Ground Flat Stock, Optical and Laser Tools, Cross Test Levels, Laser Distance Measurers, Optical Comparators, Laser Receivers for Leveling, Specialty Measuring Tools, Thread Gauges, Radius Gauges, Drill Point Gauges, Wire Gauges, Ferrous Metals, Carbon Steel, Sheet, Bar Flat Round Square, Tube Square Rectangular Round, Alloy Steel, Sheet, Bar Flat Round Square, Tube Square Rectangular Round, Stainless Steel, Sheet, Bar Flat Round Square, Tube Square Rectangular Round, Cast Iron, Ingots, Blocks, Discs, Non-Ferrous Metals, Aluminum, Sheet, Bar Flat Round Square, Tube Square Rectangular Round, Copper, Sheet, Bar Flat Round Square, Tube Square Rectangular Round, Brass, Sheet, Bar Flat Round Square, Tube Square Rectangular Round, Bronze, Sheet, Bar Flat Round Square, Tube Square Rectangular Round, High-Temperature Alloys, Nickel Alloys, Titanium Alloys, Inconel Alloys, Precious Metals, Silver, Gold, Platinum, Specialty and Exotic Metals, Zinc, Lead, Tin, Bismuth, Niobium, Tantalum, Raw Forms, Billets, Slabs, Rods, Wires, Pre-Cut Shapes and Sizes, Discs and Circles, Squares and Rectangles, Rings and Hoops, Custom Shapes upon request, Metal Surface Treatments, Anodized Metals, Powder Coated Metals, Galvanized Metals, Metalworking Supplies, Lubricants and Coolants, Abrasive Materials, Cutting Disc, Sawing Tools, Tool Maintenance Compound, Power Hammers, Pneumatic Hammers, Air-Powered Hammers, Self-Contained Hammers, Split Pneumatic and Power Forging Hammer, Mechanical Hammers, Spring Hammers, Treadle Hammers, Hydraulic Hammers, C Frame Hammers, H Frame Hammers, Hand Hammers, Cross Peen Hammers, Standard Cross Peen, Rounding Cross Peen, Straight Peen Hammers, Standard Straight Peen, Rounding Straight Peen, Sledge Hammers, Short Handle Sledge, Long Handle Sledge, Swedish Hammers, Swedish Pattern, Swedish Style with Cross Peen, German Pattern Hammers, French Pattern Hammers, French Pattern with Flat Face, French Pattern with Cross Peen, Japanese Style Hammers, Japanese Dog Head, Japanese Raising Hammer, Specialty Hammers, Rounding Hammers, Standard Rounding, Rounding with Flat Face, Planishing Hammers, Planishing Hammers, High Crown Planishing, Low Crown Planishing, Chasing Hammers, Standard Chasing, Chasing with Domed Face, Flatter Hammers, Standard Flatter, Sledge Flatter, Rivet Hammers, Rivet Hammers, Light Duty Rivet, Heavy Duty Rivet, Squaring Hammers, Square Hammer, Small Square, Large Square, Hammer Sets, Beginner Sets, Basic Hand Hammer Set, Starter Power Hammer Kit, Professional Sets, Professional Hand Hammer Set, Professional Power Hammer Kit, Customizable Sets, Build Your Own Hand Hammer Set, Build Your Own Power Hammer Kit, Hammer Accessories, Handles and Grips, Hammer Shaft, Wooden Handles, Fiberglass Handles, Handle Guards, Leather Guards, Rubber Guards, Hammer Racks and Holders, Wall-Mounted Racks, Free-Standing Holders, Replacement Heads, Interchangeable Heads, Custom Heads, Custom Engraving Options, Name Engraving, Logo Engraving, Hammer Maintenance, Hammer Dressing Tools, Grinding Stones, Filing Tools, Maintenance Kits, Hammer Care Kits, Handle Replacement Kits, Polishing Supplies, Polishing Cloths, Metal Polishes, Tongs, Flat Jaw Tongs, Wolf Jaw Tongs, V-Bit Bow Tongs, Bolt Tongs, Blade Tongs, Ring Tongs, Scrolling Tongs, Pickup Tongs, Rivet Tongs, Z-Jaw Tongs, Chainmaker's Tongs, Hollow Bit Tongs, Locking Tongs, Pliers, Long Nose Pliers, Locking Pliers Vise-Grips, Lineman's Pliers, Diagonal Pliers Side Cutters, Slip Joint Pliers, Tongue and Groove Pliers Channellocks, Wire Twisting Pliers, Snap Ring Pliers, Hose Clamp Pliers, Welding Pliers, Sheet Metal Pliers, Specialty Tongs and Pliers, Foundry Tongs, Crucible Tongs, Blacksmith Tong, Farrier Tongs, Repousse Tongs, Tong and Plier Accessories, Tong Clips-Rings, Plier Organizers-Racks, Replacement Grips, Heat Shields, Traditional Anvils, London Pattern Anvils, German Pattern Anvils, American Pattern Anvils, Double Horn Anvils - Double Bick Anvils, Single Bick Anvils, England Anvils, Ornamental Anvils, Farrier's Anvils, Specialty Anvils, Stake Anvils, Sawmaker's Anvils, Bench Anvils, Cutting Plate Anvils, Tinman's Anvils, Hornless Anvils, Portable Anvils, Railroad Track Anvils, Stake Pocket Anvils, Small Travel Anvils, Anvil Accessories, Anvil Stands wooden metal portable, Anvil Horn Caps, Anvil Cutting Plates, Anvil Hardy Tools, Swage Blocks, Standard Anvil Stands, Wooden Stands, Steel Stands, Fabricated Stand, Cast Iron Stands, Customizable Stands, Adjustable Height Stands, Modular Stands, Portable Stands, Specialty Stands, Farrier Anvil Stands, Tool Racks, Sound Dampening Stands, Stand Accessories, Stand Pads-Cushions, Tool Holders and Racks, Casters and Wheels, Anchoring Equipment, Forges, Gas Forges, Single Burner Forges, Double Burner Forges, Triple Burner Forges, Coal Forges, Portable Coal Forges, Stationary Coal Forges, Electric Forges, Induction Forges, Resistance Forges, Forge Accessories, Forge Liners and Refractory Materials, Ceramic Fiber Blankets, Refractory Bricks, Tuyeres and Air Gates, Tuyere Assemblies, Air Gate Valves, Clay and Mortar, Gas Burners, Propane Burners, Natural Gas Burners, Blowers, Hand Crank Blowers, Electric Blowers, Induction Coils, Standard Coils, Custom Coils, Temperature Control, Pyrometers, Digital Pyrometers, Analog Pyrometers, Thermocouples, Type K Thermocouples, Type N Thermocouples, Temperature Controllers, PID Controllers, On-Off Controllers, Quenching Equipment, Quench Tanks, Oil Quench Tanks, Water Quench Tanks, Quenching Oils, Fast Quench Oils, Slow Quench Oils, Quenching Accessories, Baskets and Tongs, Agitators and Coolers, Heat Treatment, Heat Treating Ovens, Benchtop Ovens, Cabinet Ovens, Heat Treating Furnaces, Box Furnaces, Tube Furnaces, Heat Treating Accessories, Quench Plates, Heat Treating Tongs, Cutting Tools, Hardy Hot Cutters, Hot Cutters, Straight Blade Hot Cutters, Curved Blade Hot Cutters, Hardy Cold Cutters, Cold Cutter, Bench Mounted Cold Cutters, Anvil Mounted Cold Cutters, Slitting Chisels, Narrow Slitting Chisels, Wide Slitting Chisels, Bench Shears, Lever Operated Bench Shears, Pedal Operated Bench Shears, Forming Tools, Hardy Swages, Top Swage, Bottom Swage, Swage Block, Bending Forks, Stone Fork, U-Shaped Bending Forks, V-Shaped Bending Forks, Fullers, Top Fullers, Bottom Fullers, Bick Irons, Bick Irons, Short Beak Irons, Long Beak Irons, Set Tools, Hardy Sets, Starter Hardy Set, Professional Hardy Set, Fuller Sets, Top Fuller Sets, Bottom Fuller Sets, Swage Sets, Round Swage Sets, Square Swage Sets, Specialty Hardy Tools, Creasing Tools, Creasing Hammer, Creasing Iron, Creasing with Horn, Edge Creasers, Groove Creasers, Flatters, Flat Surface Flatters, Square Surface Flatters, Bick Irons Bicorns, Short Horn Bick Irons, Long Horn Bick Irons, Hardy Hammers, Hardy Cut-off Hammers, Hardy Shaping Hammers, Tool Holders and Stands, Hardy Tool Racks, Wall Mounted Racks, Bench Mounted Racks, Anvil Tool Stands, Single Holder Stands, Multiple Holder Stands, Maintenance and Repair, Tool Care Kits, Cleaning and Polishing Kits, Rust Prevention Kits, Replacement Parts, Replacement Handles, Replacement Blades, Sharpening Tools, Sharpening Stones, Files and Rasps, Safety Equipment, Protective Gear, Cut Resistant Gloves, Heat Resistant Gloves, Safety Glasses, Tool Guards, Blade Guards, Edge Protectors, Power Hammers, Pneumatic Power Hammers, Pneumatic Hammers, Utility Air Hammers, Mechanical Power Hammers, Spring Helve Hammers, Mechanical Trip Hammers, Hydraulic Power Hammers, Open Die Hammers, Closed Die Hammers, Hydraulic Presses, H-Frame Presses, Manual H-Frame Presses, Motorized H-Frame Presses, C-Frame Presses, Benchtop C-Frame Presses, Floor Model C-Frame Presses, Forging Presses, Open Die Forging Presses, Closed Die Forging Presses, Power Hammer and Press Accessories, Dies and Tooling, Flat Dies, Drawing Dies, Swaging Dies, Fullering Dies, Anvil Blocks and Bases, Anvil Stands, Swage Blocks, Tong and Tool Holders, Quick Change Holders, Tong Racks, Safety Equipment, Protective Barriers, Safety Screens, Sound Dampening Panels, Noise Protection, Ear Muffs, Ear Plugs, Vibration Dampeners, Anti-Vibration Pads, Vibration-Dampening Mats, Maintenance and Repair, Lubrication Systems, Automatic Greasers, Oil and Grease Pumps, Replacement Parts, Springs and Bushings, Pistons and Cylinders, Tool Maintenance, Die Sharpening Tools, Alignment Tools, Control Systems, Foot Pedals, Single Pedal Controls, Dual Pedal Controls, Control Panels, Manual Control Panels, Automated Control Systems, Customization Options, Custom Dies, Custom Design Dies, Custom Size Dies, Custom Press Frames, Custom Load Capacity Frames, Custom Size Frames, Bench Grinders, Single Speed Bench Grinders, Light Duty Bench Grinders, Heavy Duty Bench Grinders, Variable Speed Bench Grinders, Adjustable Speed Bench Grinders, High Precision Bench Grinders, Belt Grinders, Stationary Belt Grinders, Vertical Belt Grinders, Horizontal Belt Grinders, Handheld Belt Grinders, Portable Belt Grinders, Cordless Belt Grinders, Angle Grinders, Electric Angle Grinders, Corded Angle Grinders, Cordless Angle Grinders, Pneumatic Angle Grinders, Air-Powered Angle Grinders, High-Speed Angle Grinders, Specialty Grinders, Tool Sharpening Grinders, Knife Sharpening Grinders, Chisel Sharpening Grinders, Surface Grinders, Flat Surface Grinders, Contour Surface Grinders, Cylindrical Grinders, External Cylindrical Grinders, Internal Cylindrical Grinders, Disc Sanders, Stationary Disc Sanders, Single Disc Sanders, Dual Disc Sanders, Handheld Disc Sanders, Portable Disc Sanders, Variable Speed Disc Sanders, Drum Sanders, Floor Model Drum Sanders, Single Drum Sanders, Dual Drum Sanders, Benchtop Drum Sanders, Adjustable Drum Sanders, Compact Drum Sanders, Grinder and Sander Accessories, Grinding Wheels and Discs, Abrasive Grinding Wheels, Diamond Grinding Wheels, Sanding Belts and Discs, Sanding Belts for Metal, Sanding Discs for Wood, Polishing Pads and Wheels, Wool Polishing Pads, Foam Polishing Pads, Dust Collection Systems, Dust Collectors for Grinders, Dust Bags for Sanders, Chisels Fullers and Punches, Chisels, Flat Chisels, Narrow Flat Chisels, Wide Flat Chisels, Cape Chisels, Straight Cape Chisels, Offset Cape Chisels, Diamond Point Chisels, Small Diamond Chisels, Large Diamond Chisels, Round Nose Chisels, Small Round Nose Chisels, Large Round Nose Chisels, Fullers, Top Fullers, Chisels, Fullers & Punches, Swage Blocks & Mandrels, Finishing & Polishing Tools, Forging Kits, Home page, Forging Hammers, Tongs & Pliers, Anvils & Stands, Measuring & Layout Tools, Hardy Tools, Protective Gear, Quenching Oils & Fluids, Grinders & Sanders, Material Stock (Metals & Alloys), Forges & Burners, Forge Parts & Accessories, Heating Equipment, Blacksmithing Aprons, Power Hammers & Presses, Decorative Hardware & Fasteners, Head & Face Protection, Safety Goggles and Glasses, Full Face Shields and Face Visors, Welding Helmets, Heat-Resistant Face Masks, Protective Headbands and Caps, Hearing Protection, Noise-Canceling Ear Muffs, Ear Plugs, High Fidelity Ear Protectors for Forge Work, Hand and Arm Protection, Leather Forge Gloves, Cut-Resistant Gloves, Arm Guards and Sleeves, Vibration-Dampening Gloves, High-Temperature Welding Gloves, Aluminized Oversleeves, Water-Proof Latex Gloves, Welders Oversleeves, Body Protection, Leather Aprons, Hydration and Repair Hand Creams, High-Visibility Gear, Reflective Safety Vests, High-Visibility Shirts and Jackets, LED Safety Bands and Lights, Glow in the Dark Tape and Markings, Cooling Gear, Cooling Vests and Jackets, Neck Cooling Wraps, Cooling Bandanas and Headbands, Hydration Packs with Cooling Technology, Supportive Gear, Back Support Belts, Knee Pads and Cushions, Anti-Fatigue Floor Mats, Wrist Support and Compression Gloves, Emergency and First Aid, Burn Kits and Gels, First Aid Kits for Workshops, Eye Wash Stations, Fire Extinguishers and Blankets, Emergency Escape Masks, Rulers and Measuring Tapes, Steel Ruler, Fiberglass Tape Measure, Hook Rulers for Precision, Folding Rulers, Digital Measuring Wheel, Calipers and Micrometers, Calipers, Digital Calipers, Inside and Outside Micrometers, Dial Calipers, Depth Micrometers, Squares and Angles, Try Squares, Framing Squares, Sliding Bevels, Angle Finders, Combination Squares, Levels and Plumb Bobs, Spirit Levels Various Sizes, Tripod Laser Levels, Torpedo Levels, Plumb Bobs, Line Levels, Marking Tools, Soapstone Markers, Metal Scribing Tools, Chalk Line Reels, Punches for Marking, Marking Gauges, Protractors and Compasses, Digital Protractors, Angle Protractors, Wing and Traditional Compasses, Dividers for Precision Layout"
    
    prompt = f"Read the {body} of this product. Understand what it is. This is a blacksmithing supplies shop. You must generate 5 tags for this product {title} with option {option1_value} This is the title and description of the product.. The tags must be selected extremely carefully. Try to make them as relevant as possible to the product category. Do not just select the top one. They must fit exactly what the product is. This is to put products into a collection, so every tag you use will add the product to that collection, therefore it must be as accurate as possible. Do not chat back to me, just list with commas separating 5 tags minimum. You must select from this list of tags {possible_tags}"

    try:
        client = anthropic.Anthropic(api_key=anthropic_api_key)
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=150,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        generated_tags = response.content[0].text.strip()
        print(f"Generated tags for '{title}': {generated_tags}")
        return generated_tags
    except Exception as e:
        print(f"Error generating tags for '{title}': {str(e)}")
        return None

# Main function to process products and generate tags
def process_products(products_csv, output_csv):
    # Read product data
    with open(products_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        products = list(reader)
    
def process_products(products_csv, output_csv):
    # Read product data
    with open(products_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        products = list(reader)
    
    # Prepare output CSV
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Handle', 'Title', 'Option1 Value', 'Generated Tags'] + reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for product in products:
            title = product['Title']
            body = product.get('Description', '')
            option1_value = product.get('Option1 Value', '')
            
            if not title:
                writer.writerow({key: '' for key in fieldnames})  # Writes a blank row
                continue
            
            generated_tags = generate_tags(title, body, option1_value)
            
            product_data = {
                'Handle': product['Handle'],
                'Title': title,
                'Option1 Value': option1_value,
                'Generated Tags': generated_tags
            }
            product_data.update(product)
            writer.writerow(product_data)

    print("Processing complete. Output file created:", output_csv)

# Example usage
if __name__ == "__main__":
    products_csv = 'ANVILS CSV - Sheet1[1].csv'  # Input CSV file containing products
    output_csv = 'output_with_tags.csv'  # Output CSV file to store products with generated tags

    process_products(products_csv, output_csv)
