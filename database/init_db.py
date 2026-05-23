from app import app, db, Analysis, Statistics
from datetime import datetime

with app.app_context():
    # Drop all tables
    db.drop_all()
    
    # Create all tables
    db.create_all()
    
    # Create initial statistics record
    stats = Statistics()
    db.session.add(stats)
    
    # Add sample data
    sample_analyses = [
        Analysis(
            market='EUR/USD',
            direction='LONG',
            timeframe='15m',
            tips='["Wait for confirmation at support level", "Use proper risk management"]',
            confidence=85,
            raw_subtitle='EUR/USD showing bullish signals on 15m timeframe. Wait for confirmation at 1.0850 support level before entering a long position.',
            timestamp=datetime.utcnow()
        ),
        Analysis(
            market='GBP/USD',
            direction='SHORT',
            timeframe='1h',
            tips='["Watch for break below resistance", "Set stop loss above 1.2650"]',
            confidence=75,
            raw_subtitle='GBP/USD looking bearish on 1h chart. Watch for a break below the resistance at 1.2650.',
            timestamp=datetime.utcnow()
        )
    ]
    
    for analysis in sample_analyses:
        db.session.add(analysis)
    
    db.session.commit()
    
    print('✅ Database initialized with sample data')
