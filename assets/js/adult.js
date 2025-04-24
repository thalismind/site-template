const LS_ADULT_KEY = "adult";
const MODES = {
    ADULT: "adult",
    ANGEL: "angel",
};

window.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    const config = body.getAttribute("data-adult");

    const getAdultState = () => {
        const lsState = localStorage.getItem(LS_ADULT_KEY);
        if (lsState) return lsState;

        let state;
        switch (config) {
            case MODES.ADULT:
                state = MODES.ANGEL;
                break;
            case MODES.ANGEL:
                state = MODES.ADULT;
                break;
            default:
                state = MODES.ANGEL;
                break;
        }
        return state;
    };

    const setAdult = (state) => {
        if (state === MODES.ADULT) {
            document.documentElement.classList.add(MODES.ADULT);
            document.documentElement.classList.remove(MODES.ANGEL);
        } else if (state === MODES.ANGEL) {
            document.documentElement.classList.remove(MODES.ADULT);
            document.documentElement.classList.add(MODES.ANGEL);
        }
    };

    setAdult(getAdultState());

    const toggleAdult = () => {
        const state = getAdultState();
        if (state === MODES.ADULT) {
            localStorage.setItem(LS_ADULT_KEY, MODES.ANGEL);
            setAdult(MODES.ANGEL);
        } else if (state === MODES.ANGEL) {
            localStorage.setItem(LS_ADULT_KEY, MODES.ADULT);
            setAdult(MODES.ADULT);
        }
    };


    const adult = document.getElementById('adult');
    if (adult) {
      adult.addEventListener('click', () => toggleAdult());
    }
})