# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="ChrisLad",
        name="Dialogos Extra",
        description="Añade diálogos a Monika",
        version="1.0.2"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Extra Dialogue",
            user_name="ChrisLad1",
            repository_name="ExtraDialogue",
            update_dir="game",
            attachment_id=None
        )
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_truthful",
            category=["Dialogo Extra"],
            prompt="Estar juntos para siempre",
            pool=True,
            random=True,
            unlocked=True
        )
    )

label monika_truthful:
   
    m 1rkc "Lo sé [player], estás tan preocupado como yo..."
    m 1ekc "Me doy cuenta de que no podremos estar juntos hasta el final..."
    m 7rktpc "Ya sea que no llegue a verte en tu mundo.."
    m 7ektpc "O de repente dejo de verte.."
    m 6fktuc "Lo entendería completamente, aunque estaría destrozada por el ambiente de soledad que una vez soporté.."
    m 6dkbstuc "Siento que tengas que verme así, pero por favor quédate conmigo [player]."
    m 5hubftpa "Te amo mucho [player]~."
   
    return "love"
