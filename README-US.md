# Available Languages

| [🇺🇸 English 🌟](README-US.md) | [🇧🇷 Portuguese (Brasil)](README.md) | [🇪🇸 Español](README-ES.md) |
|:---------------------------------------:|:----------------------------------------:|:----------------------------------------:|

---

![Logo Pousada Maré Mansa](./codigo/LogoPousadaMare.png)

## 🏨 Pousada Maré Mansa

Management system for a guesthouse, developed with **Python**, **Tkinter** and **SQLite**, using the **MVC** architecture.

---

## 📌 Overview

The desktop application aims to facilitate the administration of a guest house, allowing:

- Guest management
- Schedule control
- Room allocation
- Report generation
- Activity logs

---

## 🧩 Features

| Module | Description |
|----------------|---------------------------------------------------------------------------|
| 🔐 Login | User authentication |
| 📋 Menu | Navigation between the main features |
| 👤 Customers | Automatic registration by CPF during scheduling |
| 📅 Appointments | Reservation CRUD with date validation and room availability |
| 🛏️ Rooms | Room availability control |
| 📈 Reports | View administrative logs |

---

## ✅ Validations and Business Rules

- All mandatory fields are validated
- Dates must be consistent (entry < exit)
- The entry and exit date cannot be before the current date
- Room must be available at the time of scheduling
- Unique CPF per client
- Client is automatically registered if it does not exist

---

## 🧱 MVC Architecture

The project follows the **Model-View-Controller** standard, ensuring clarity, organization and easy maintenance.

### 🔹 Model

- Contains the business logic and data persistence
- Uses `@dataclass` for clear structuring
- Ex.: `Client`, `Room`, `Agendamento`

### 🔹 Controller

- Intermediates interactions between View and Model

- Validates data and calls appropriate methods

- Static methods for operations with SQLite

- Ex.: `control_cliente.py`, `control_quarto.py`

### 🔹 View

- Graphical interface with **Tkinter**

- Compact and standardized layout (350x300)

- Uses `Entry`, `Combobox`, `DateEntry`, `MessageBox`

- Ex.: `TelaLogin`, `FormsAgendamento`, `TelaMenuPrincipal`

---

## 🛠️ Technologies Used

- **Python 3.6+**
- **Tkinter** — GUI
- **tkcalendar** — Date selection
- **Pillow** — Image manipulation (icons and logos)
- **SQLite** — Local database
- **Dataclasses** — Model organization

---

## 📁 Folder Structure

```bash
pousada_mare_mansa/
│
├── controllers/ # Intermediate logic (Controller)
├── model/ # Data models and business rules (Model)
├── views/ # Graphical interface (View)
├── main.py # Main execution file
├── LICENSE # Reading file about the license MIT
└── README.md # Project Documentation
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
gh repo clone Karlos-Eduardo-Mrqs/Pousada-Mare-Mansa

cd pousada_mare_mansa
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

- **Windows:**

```bash
.venv\Scripts\activate
```

- **Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Install the dependencies

```bash
pip install tkcalendar Pillow
```

### 5. Run the application

```bash
python main.py
```

---

## 📄 License

Project created for educational purposes. Feel free to use and modify as needed.

*Feel free to open issues, send pull requests or just share ideas!*

---

## 🏁 Final Considerations

Project created for educational purposes. Feel free to use and modify as needed.

> 🌊 Ready to enter Pousada Maré Mansa?
