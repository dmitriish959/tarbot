from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import os
from dotenv import load_dotenv

load_dotenv()

tar_zn = {
    "l2": [8395, 10140],
    "l3": [8540, 10480],
    "l4": [8685, 10820],
    "l5": [8830, 11160],
    "l6": [8975, 11500],
    "l7": [9120, 11840],
    "l8": [9265, 12180],
    "l9": [9410, 12520],
    "l10": [9555, 12860],
    "l11": [9700, 13200],
    "l12": [9845, 13540],
    "l13": [9990, 13880],
    "l14": [10135, 14220],
    "l15": [10280, 14560],
    "l16": [10425, 14900],
    "l17": [10570, 15240],
    "l18": [10715, 15580],
    "l19": [10860, 15920],
    "l20": [11005, 16260],
    "l21": [11150, 16600],
    "l22": [11295, 16940],
    "l23": [11440, 17280],
    "l24": [11585, 17620],
    "l25": [11730, 17960],
    "l26": [11875, 18300],
    "l27": [12020, 18640],
    "l28": [12165, 18980],
    "l29": [12310, 19320],
    "l30": [12455, 19660],
    "l31": [12600, 20000],
    "l32": [12745, 20340],
    "l33": [12890, 20680],
    "l34": [13035, 21020],
    "l35": [13180, 21360],
    "l36": [13325, 21700],
    "l37": [13470, 22040],
    "l38": [13615, 22380],
    "l39": [13760, 22720],
    "l40": [13905, 23060],
    "l41": [14050, 23400],
    "l42": [14195, 23740],
    "l43": [14340, 24080],
    "l44": [14485, 24420],
    "l45": [14630, 24760],
    "l46": [14775, 25100],
    "l47": [14920, 25440],
    "l48": [15065, 25780],
    "l49": [15210, 26120],
    "l50": [15355, 26460],
    "l51": [15500, 26800],
    "l52": [15750, 27200],
    "l53": [16000, 27600],
    "l54": [16250, 28000],
    "l55": [16500, 28400],
    "l56": [16750, 28800],
    "l57": [17000, 29200],
    "l58": [17250, 29600],
    "l59": [17500, 30000],
    "l60": [17750, 30400],
    "l61": [18000, 30800],
    "l62": [18250, 31200],
    "l63": [18500, 31600],
    "l64": [18750, 32000],
    "l65": [19000, 32400],
    "l66": [19250, 32800],
    "l67": [19500, 33200],
    "l68": [19750, 33600],
    "l69": [20000, 34000],
    "l70": [20250, 34400],
    "l71": [20500, 34800],
    "l72": [20750, 35200],
    "l73": [21000, 35600],
    "l74": [21250, 36000],
    "l75": [21500, 36400],
    "l76": [21750, 36800],
    "l77": [22000, 37200],
    "l78": [22250, 37600],
    "l79": [22500, 38000],
    "l80": [22750, 38400],
    "l81": [23000, 38800],
    "l82": [23250, 39200],
    "l83": [23500, 39600],
    "l84": [23750, 40000],
    "l85": [24000, 40400],
    "l86": [24250, 40800],
    "l87": [24500, 41200],
    "l88": [24750, 41600],
    "l89": [25000, 42000],
    "l90": [25250, 42400],
    "l91": [25500, 42800],
    "l92": [25750, 43200],
    "l93": [26000, 43600],
    "l94": [26250, 44000],
    "l95": [26500, 44400],
    "l96": [26750, 44800],
    "l97": [27000, 45200],
    "l98": [27250, 45600],
    "l99": [27500, 46000],
    "l100": [27750, 46400],
}

MAIN_MENU, DUT_INPUT, TANK_STEP_INPUT, TANK_MAX_INPUT = range(4)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["Обучение ДУТ", "Таблица тарировки бака"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    await update.message.reply_text("Выберите раздел:", reply_markup=markup)
    return MAIN_MENU


async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()

    if text == "обучение дут":
        await update.message.reply_text(
            "Введите длину трубки ДУТ (например, 51). Для выхода в меню введите 0:",
            reply_markup=ReplyKeyboardMarkup([["Меню"]], resize_keyboard=True),
        )
        return DUT_INPUT

    elif text == "таблица тарировки бака":
        await update.message.reply_text(
            "Введите шаг измерения в литрах (например, 50):",
            reply_markup=ReplyKeyboardMarkup([["Меню"]], resize_keyboard=True),
        )
        return TANK_STEP_INPUT

    else:
        await update.message.reply_text("Неверный выбор. Попробуйте снова:")
        return MAIN_MENU


async def handle_dut(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.lower() == "меню" or text == "0":
        return await start(update, context)

    try:
        n = int(text)
        key = f"l{n}"
        if key in tar_zn:
            value = tar_zn[key]
            await update.message.reply_text(
                f"Значение для {key}: {value}\nВведите следующую длину трубки или 0 для выхода в меню:"
            )
        else:
            await update.message.reply_text(f"Значение для {key} не найдено. Попробуйте снова:")
    except ValueError:
        await update.message.reply_text("Введите число!")

    return DUT_INPUT


async def handle_tank_step(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.lower() == "меню" or text == "0":
        return await start(update, context)

    try:
        step = int(text)
        if step <= 0:
            await update.message.reply_text("Шаг должен быть положительным числом.")
            return TANK_STEP_INPUT
        context.user_data["tank_step"] = step
        await update.message.reply_text("Введите максимальный объём бака в литрах:")
        return TANK_MAX_INPUT
    except ValueError:
        await update.message.reply_text("Введите число!")
        return TANK_STEP_INPUT


async def handle_tank_max(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.lower() == "меню" or text == "0":
        return await start(update, context)

    try:
        max_volume = int(text)
        if max_volume <= 0:
            await update.message.reply_text("Объём должен быть положительным числом.")
            return TANK_MAX_INPUT

        step = context.user_data.get("tank_step", 50)
        table = []
        for vol in range(0, max_volume + step, step):
            table.append(f"{vol} л")

        await update.message.reply_text(
            "Таблица тарировки бака:\n" + "\n".join(table) +
            "\n\nВведите 'Меню' или 0 для возврата."
        )
        return TANK_MAX_INPUT
    except ValueError:
        await update.message.reply_text("Введите число!")
        return TANK_MAX_INPUT


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Операция отменена.")
    return ConversationHandler.END


def main():
    token = os.getenv("tok_bot")
    if not token:
        raise ValueError("Токен бота не найден! Проверь .env файл.")

    app = Application.builder().token(token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAIN_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu)],
            DUT_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_dut)],
            TANK_STEP_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_tank_step)],
            TANK_MAX_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_tank_max)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()