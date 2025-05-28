import tkinter as tk
from app.app import TryYourLuckApp
import logging

def configure_logging():
    logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Давай сыграем")

if __name__ == "__main__":
    configure_logging()
    root = tk.Tk()
    app = TryYourLuckApp(root)
    
    tk.messagebox.showwarning(
        "Внимание", 
        "Эта игра не для слабаков! Сыграем?"
    )
    
    root.mainloop()