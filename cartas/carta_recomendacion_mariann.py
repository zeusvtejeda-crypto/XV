from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.units import cm

out = "cartas/Carta_Recomendacion_Mariann_Danae_Huerta_Alvarez.pdf"
doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=3*cm, rightMargin=3*cm, topMargin=2.5*cm, bottomMargin=2.5*cm)
b = ParagraphStyle("b", fontName="Helvetica", fontSize=11.5, leading=19, alignment=TA_JUSTIFY, firstLineIndent=1.2*cm, spaceAfter=10)
s = []
s += [Paragraph("CARTA DE RECOMENDACIÓN", ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=17)),
      HRFlowable(width="100%", thickness=1.2, color="black", spaceBefore=4), Spacer(1, 30),
      Paragraph("12 de octubre de 2026", ParagraphStyle("d", fontName="Helvetica", fontSize=12, alignment=TA_RIGHT)), Spacer(1, 30),
      Paragraph("<b>A QUIEN CORRESPONDA:</b>", ParagraphStyle("a", fontName="Helvetica", fontSize=11.5)), Spacer(1, 14),
      Paragraph("Me permito informarle que conozco amplia y detalladamente a la C. <b>Mariann Danae Huerta Álvarez</b> y puedo asegurar que es una persona íntegra, estable, totalmente responsable y competente para cualquier tipo de actividad que se le encomiende, de acuerdo a los alcances especificados en su Carta de Presentación o Curricular.", b),
      Paragraph("Por lo anterior no tengo inconveniente alguno en recomendarla ampliamente, agradeciendo de antemano la atención y facilidades que le puedan brindar.", b),
      Spacer(1, 8),
      Paragraph("Se extiende la presente para los efectos legales que a la interesada convenga.", b),
      Spacer(1, 70),
      HRFlowable(width="55%", thickness=0.8, color="black"),
      Paragraph("Lourdes Lizbeth Huerta Villaseñor", ParagraphStyle("n", fontName="Helvetica-Bold", fontSize=12, alignment=TA_CENTER, spaceBefore=4)),
      Paragraph("Nombre y firma de la otorgante", ParagraphStyle("f", fontName="Helvetica", fontSize=10, alignment=TA_CENTER)),
      Spacer(1, 26),
      Paragraph("<b>Teléfono:</b> 311 890 3298", ParagraphStyle("tel", fontName="Helvetica", fontSize=11, spaceAfter=4)),
      Paragraph("<b>Correo electrónico:</b> lizbethhuertavillasenor@gmail.com", ParagraphStyle("c", fontName="Helvetica", fontSize=11))]
doc.build(s)
