from pdf2image import convert_from_path
from PIL import Image
import os

def cylinder_transition_effect(input_image_path1, input_image_path2, output_folder, num_frames=10, pause_frames=5, scale_factor=0.5):
    # Konvertiere die PDF-Seiten in Bilder
    images1 = convert_from_path(input_image_path1)
    images2 = convert_from_path(input_image_path2)

    # Nimm nur die erste Seite, falls mehrere Seiten vorhanden sind
    image1 = images1[0]
    image2 = images2[0]

    # Bestimmen der maximalen Breite und Höhe
    max_width = max(image1.width, image2.width)
    max_height = max(image1.height, image2.height)

    # Optional: Skalierung der Bilder, um die Dateigröße weiter zu reduzieren
    max_width = int(max_width * scale_factor)
    max_height = int(max_height * scale_factor)

    # Beide Bilder auf die maximale Größe skalieren
    image1 = image1.resize((max_width, max_height), Image.LANCZOS)
    image2 = image2.resize((max_width, max_height), Image.LANCZOS)

    width, height = image1.size

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_index = 1

    # Erstellen der Übergangsframes von Bild1 zu Bild2
    for frame in range(num_frames + 1):
        new_image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

        offset = int((width * frame) / num_frames)
        part1 = image1.crop((offset, 0, width, height))
        part2 = image2.crop((0, 0, offset, height))

        new_image.paste(part1, (0, 0))
        new_image.paste(part2, (width - offset, 0))

        frame_path = os.path.join(output_folder, f"frame{frame_index}.pdf")
        new_image.convert("RGB").save(frame_path, "PDF")
        frame_index += 1

    # Pause-Frames für Bild2 hinzufügen
    for frame in range(pause_frames):
        frame_path = os.path.join(output_folder, f"frame{frame_index}.pdf")
        image2.convert("RGB").save(frame_path, "PDF")
        frame_index += 1

    # Erstellen der Übergangsframes von Bild2 zurück zu Bild1
    for frame in range(num_frames + 1):
        new_image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

        offset = int((width * frame) / num_frames)
        part1 = image2.crop((offset, 0, width, height))
        part2 = image1.crop((0, 0, offset, height))

        new_image.paste(part1, (0, 0))
        new_image.paste(part2, (width - offset, 0))

        frame_path = os.path.join(output_folder, f"frame{frame_index}.pdf")
        new_image.convert("RGB").save(frame_path, "PDF")
        frame_index += 1

    # Pause-Frames für Bild1 hinzufügen
    for frame in range(pause_frames):
        frame_path = os.path.join(output_folder, f"frame{frame_index}.pdf")
        image1.convert("RGB").save(frame_path, "PDF")
        frame_index += 1

# Beispielaufruf mit PDF-Dateien
cylinder_transition_effect("test1.pdf", "test2.pdf", "frames_cylinder_new", num_frames=31, pause_frames=12, scale_factor=0.5)
