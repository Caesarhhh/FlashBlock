import os
import glob
from collections import defaultdict

VIDEO_ROOT = "demo/demo_videos"
cats = ["Complex_Landscape", "Human_Identity", "Motion_Rationality"]

html_output = []

for cat in cats:
    cat_path = os.path.join(VIDEO_ROOT, cat)
    if not os.path.exists(cat_path):
        continue
    
    html_output.append(f'<div class="category-title">{cat.replace("_", " ")}</div>')
    html_output.append('<div class="comparison-grid">')
    
    # Get all prompts (filenames without the -0.mp4 suffix usually)
    # Recursively find all mp4s in 'ours' to identify unique prompts
    # 'baseline' should have matching ones
    
    ours_path = os.path.join(cat_path, "ours")
    baseline_path = os.path.join(cat_path, "baseline")
    
    # Get list of files in 'ours'
    if not os.path.exists(ours_path):
        continue
        
    files = sorted([f for f in os.listdir(ours_path) if f.endswith(".mp4")])[:4]
    
    for f in files:
        # f is like "A man is dancing.-0.mp4"
        prompt = f.replace("-0.mp4", "")
        
        # Paths relative to index.html
        ours_rel = os.path.join(VIDEO_ROOT, cat, "ours", f)
        baseline_rel = os.path.join(VIDEO_ROOT, cat, "baseline", f)
        
        # Check if baseline exists
        has_baseline = os.path.exists(baseline_rel)
        
        # Generate Cards
        
        # Baseline Card
        if has_baseline:
            html_output.append(f'''
            <div class="video-card">
                <div class="video-wrapper">
                    <video controls preload="metadata">
                        <source src="{baseline_rel}" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
                <div class="video-caption">
                    <span class="badge badge-baseline">Baseline</span>
                    <div>{prompt}</div>
                </div>
            </div>
            ''')
            
        # Ours Card
        html_output.append(f'''
        <div class="video-card">
            <div class="video-wrapper">
                <video controls preload="metadata">
                    <source src="{ours_rel}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            <div class="video-caption">
                <span class="badge badge-ours">Ours</span>
                <div>{prompt}</div>
            </div>
        </div>
        ''')

    html_output.append('</div>') # End grid

print("\n".join(html_output))
