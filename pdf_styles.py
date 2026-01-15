from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import TableStyle

# Create a new stylesheet
global_styles = getSampleStyleSheet()

# Create a new style sheet to avoid modifying the base one
custom_styles = {}

# Base styles
base_style = {
    'fontName': 'Helvetica',
    'fontSize': 10,  # Slightly smaller font for better fit
    'leading': 12,   # Tighter line spacing
    'spaceAfter': 8, # Reduced space after paragraphs
    'wordWrap': 'CJK',
    'leftIndent': 0,  # Ensure no left indentation
    'rightIndent': 0, # Ensure no right indentation
    'firstLineIndent': 0,
}

# Main styles
normal_style = base_style.copy()

custom_styles['Normal'] = ParagraphStyle(
    name='Normal',
    parent=global_styles['Normal'],
    alignment=TA_JUSTIFY,  # Set alignment here
    **normal_style
)

# Heading styles
for i in range(1, 6):
    custom_styles[f'Heading{i}'] = ParagraphStyle(
        name=f'Heading{i}',
        parent=global_styles[f'Heading{i}'],
        fontSize=16 - (i * 2),
        leading=18 - (i * 2),
        spaceAfter=4 + (i * 2),
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#2c3e50')
    )

# Specialized styles
styles = {
    'Subtitle': ParagraphStyle(
        name='Subtitle',
        parent=global_styles['Heading2'],
        fontSize=14,
        leading=16,
        spaceAfter=10,
        textColor=colors.HexColor('#7f8c8d')
    ),
    'Section': ParagraphStyle(
        name='Section',
        parent=global_styles['Heading3'],
        fontSize=12,
        leading=14,
        spaceAfter=6,
        textColor=colors.HexColor('#2c3e50'),
        borderWidth=1,
        borderColor=colors.HexColor('#bdc3c7'),
        borderPadding=(0, 0, 5, 0)
    ),
    'Quote': ParagraphStyle(
        name='Quote',
        parent=global_styles['Normal'],
        fontSize=10,
        leading=12,
        leftIndent=20,
        textColor=colors.HexColor('#7f8c8d'),
        borderLeftWidth=3,
        borderLeftColor=colors.HexColor('#bdc3c7'),
        borderLeftPadding=10,
        spaceAfter=10
    ),
    'Footer': ParagraphStyle(
        name='Footer',
        parent=global_styles['Normal'],
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#7f8c8d'),
        alignment=TA_CENTER
    )
}

# Table styles
table_styles = {
    'default': [
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#003366')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2c3e50')),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dddddd')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#dddddd')),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ],
    'landscape': [
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#003366')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2c3e50')),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dddddd')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#dddddd')),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2c3e50')),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dddddd')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#dddddd')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]
}

# Add LEFT, CENTER, RIGHT alignment helpers
for align, name in [(TA_LEFT, 'Left'), (TA_CENTER, 'Center'), (TA_RIGHT, 'Right')]:
    style_name = f'Align{name}'
    if style_name not in global_styles:
        style = ParagraphStyle(
            name=style_name,
            parent=global_styles['Normal'],
            alignment=align
        )
        global_styles.add(style)
        globals()[name.upper()] = style
    else:
        globals()[name.upper()] = global_styles[style_name]

# Export styles
__all__ = ['global_styles', 'table_styles'] + list(styles.keys()) + ['LEFT', 'CENTER', 'RIGHT']