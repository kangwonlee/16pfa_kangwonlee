outer_diameter_mm = 50
inner_diameters_mm = (40, 20, 30, 20, 10)
length_mm = 100
section_lengths_mm = (15, 20, 15, 20, 30)

outer_radius_mm = outer_diameter_mm * 0.5
inner_radius_mm = []
for di_mm in inner_diameters_mm:
    inner_radius_mm.append(di_mm * 0.5)

upper_coordinates_mm = [(length_mm, outer_radius_mm),
                        (0.0, outer_radius_mm),
                        ]
x = 0.0
for ri_mm, section_length_mm in zip(inner_radius_mm, section_lengths_mm):
    upper_coordinates_mm.append((x, ri_mm))
    x += section_length_mm
    upper_coordinates_mm.append((x, ri_mm))

print upper_coordinates_mm
