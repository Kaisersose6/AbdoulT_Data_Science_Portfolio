from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(trace, data, output_path='report.pdf'):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    story.append(Paragraph("Marketing Mix Modeling Report", styles['Title']))
    story.append(Spacer(1, 12))
    
    # Channel contributions
    story.append(Paragraph("Channel Effectiveness", styles['Heading2']))
    img_path = "channel_effectiveness.png"
    save_coef_plot(trace, img_path)  # Implement plotting
    story.append(Image(img_path, width=400, height=300))
    
    # ROI analysis
    story.append(Paragraph("ROI Analysis", styles['Heading2']))
    roi = calculate_roi(trace, data)
    roi_text = "<br/>".join([f"{ch}: ${val:.2f} revenue per $1k spend" for ch, val in roi.items()])
    story.append(Paragraph(roi_text, styles['Normal']))
    
    # Budget recommendation
    story.append(Paragraph("Optimal Budget Allocation", styles['Heading2']))
    optimal = optimize_budget(1000000, roi)
    alloc_text = "<br/>".join([f"{ch}: ${amt:,.0f}" for ch, amt in optimal.items()])
    story.append(Paragraph(alloc_text, styles['Normal']))
    
    doc.build(story)