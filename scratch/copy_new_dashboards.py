import shutil
import os
import sys

# Ensure UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

src_dir = 'assets/images'
mapping = {
    'dashboard_dangnhap.png': 'ui_login.png',
    'giaodiệnQuảnlýSeries.png': 'ui_series.png',
    'giaodiệnQuảnlýChapter.png': 'ui_chapter.png',
    'giaodiệnQuảnlýTask.png': 'ui_task.png',
    'giaodiệnNộpSubmission.png': 'ui_submission.png',
    'giaodiệnReviewbảnthảo.png': 'ui_review.png',
    'giaodiệnThôngbáohệthống.png': 'ui_notification.png',
    'giaodiệnBảngxếphạngSeries.png': 'ui_ranking.png',
}

for src_name, dst_name in mapping.items():
    src_path = os.path.join(src_dir, src_name)
    dst_path = os.path.join(src_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied {src_name} to {dst_name}")
    else:
        print(f"Warning: {src_name} not found!")
