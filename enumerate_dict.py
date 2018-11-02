preds = {'class_ids': [1,2,3], 'scores': [0.99, 0.978, 0.88]}
preds['class_ids'] = [preds['class_ids'][i] for i, score in enumerate(preds['scores']) if score > 0.9]