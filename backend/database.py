
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "multilingua.db"


def get_connection():

    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            message TEXT NOT NULL,

            language TEXT NOT NULL,

            predicted_department TEXT NOT NULL,

            confidence REAL NOT NULL,

            status TEXT NOT NULL,

            corrected_department TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()

    connection.close()


def save_prediction(
    message,
    language,
    department,
    confidence,
    status
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO predictions (
            message,
            language,
            predicted_department,
            confidence,
            status
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        message,
        language,
        department,
        confidence,
        status
    ))

    prediction_id = cursor.lastrowid

    connection.commit()

    connection.close()

    return prediction_id


def get_predictions(status=None):

    connection = get_connection()

    cursor = connection.cursor()

    if status:

        cursor.execute(
            "SELECT * FROM predictions WHERE status = ? ORDER BY id DESC",
            (status,)
        )

    else:

        cursor.execute(
            "SELECT * FROM predictions ORDER BY id DESC"
        )

    rows = cursor.fetchall()

    connection.close()

    return [dict(row) for row in rows]


def update_review(prediction_id, corrected_department):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE predictions

        SET corrected_department = ?,
            status = 'REVIEWED'

        WHERE id = ?
        AND status = 'HUMAN_REVIEW'
    """, (
        corrected_department,
        prediction_id
    ))

    updated = cursor.rowcount

    connection.commit()

    connection.close()

    return updated
