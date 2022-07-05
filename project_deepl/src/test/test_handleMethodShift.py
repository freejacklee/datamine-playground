import json

from algo import handlePayload


def get_added_spaces(id: int):
    return 2 if (id + 3) % 13 == 0 or (id + 5) % 29 == 0 else 1


def validateHandleMethod():
    s = '{"jsonrpc":"2.0","method": "LMT_handle_jobs","params":{"jobs":[{"kind":"default","sentences":[{"text":"The Visual-Inertial Direct Sparse Odometry (VI-DSO) algorithm [70] is based on the already presented DSO algorithm [31].","id":0,"prefix":" "}],"raw_en_context_before":[],"raw_en_context_after":["The algorithm searches to minimize an energy function that combines the photometric and inertial errors, which is built considering a nonlinear dynamic model."],"preferred_num_beams":1},{"kind":"default","sentences":[{"text":"The algorithm searches to minimize an energy function that combines the photometric and inertial errors, which is built considering a nonlinear dynamic model.","id":1,"prefix":""}],"raw_en_context_before":["The Visual-Inertial Direct Sparse Odometry (VI-DSO) algorithm [70] is based on the already presented DSO algorithm [31]."],"raw_en_context_after":["Figure 18 shows an overview of the VI-DSO algorithm that illustrates its main differences concerning the DSO technique."],"preferred_num_beams":1},{"kind":"default","sentences":[{"text":"Figure 18 shows an overview of the VI-DSO algorithm that illustrates its main differences concerning the DSO technique.","id":2,"prefix":""}],"raw_en_context_before":["The Visual-Inertial Direct Sparse Odometry (VI-DSO) algorithm [70] is based on the already presented DSO algorithm [31].","The algorithm searches to minimize an energy function that combines the photometric and inertial errors, which is built considering a nonlinear dynamic model."],"raw_en_context_after":["The VI-DSO is an extension of DSO that considers the inertial information, which results in better accuracy and robustness than the original DSO and other algorithms, like ROVIO [70]."],"preferred_num_beams":1},{"kind":"default","sentences":[{"text":"The VI-DSO is an extension of DSO that considers the inertial information, which results in better accuracy and robustness than the original DSO and other algorithms, like ROVIO [70].","id":3,"prefix":""}],"raw_en_context_before":["The Visual-Inertial Direct Sparse Odometry (VI-DSO) algorithm [70] is based on the already presented DSO algorithm [31].","The algorithm searches to minimize an energy function that combines the photometric and inertial errors, which is built considering a nonlinear dynamic model.","Figure 18 shows an overview of the VI-DSO algorithm that illustrates its main differences concerning the DSO technique."],"raw_en_context_after":["However, the initialization procedure relies on bundle adjustment, which makes the initialization slow [22]."],"preferred_num_beams":1},{"kind":"default","sentences":[{"text":"However, the initialization procedure relies on bundle adjustment, which makes the initialization slow [22].","id":4,"prefix":""}],"raw_en_context_before":["The Visual-Inertial Direct Sparse Odometry (VI-DSO) algorithm [70] is based on the already presented DSO algorithm [31].","The algorithm searches to minimize an energy function that combines the photometric and inertial errors, which is built considering a nonlinear dynamic model.","Figure 18 shows an overview of the VI-DSO algorithm that illustrates its main differences concerning the DSO technique.","The VI-DSO is an extension of DSO that considers the inertial information, which results in better accuracy and robustness than the original DSO and other algorithms, like ROVIO [70]."],"raw_en_context_after":["The algorithm does not perform global optimization and loop closure detection, and embedded implementations were not found in the literature."],"preferred_num_beams":1},{"kind":"default","sentences":[{"text":"The algorithm does not perform global optimization and loop closure detection, and embedded implementations were not found in the literature.","id":5,"prefix":""}],"raw_en_context_before":["The Visual-Inertial Direct Sparse Odometry (VI-DSO) algorithm [70] is based on the already presented DSO algorithm [31].","The algorithm searches to minimize an energy function that combines the photometric and inertial errors, which is built considering a nonlinear dynamic model.","Figure 18 shows an overview of the VI-DSO algorithm that illustrates its main differences concerning the DSO technique.","The VI-DSO is an extension of DSO that considers the inertial information, which results in better accuracy and robustness than the original DSO and other algorithms, like ROVIO [70].","However, the initialization procedure relies on bundle adjustment, which makes the initialization slow [22]."],"raw_en_context_after":[],"preferred_num_beams":1}],"lang":{"preference":{"weight":{},"default":"default"},"source_lang_computed":"EN","target_lang":"ZH"},"priority":1,"commonJobParams":{"browserType":1,"formality":null},"timestamp":1657019146596},"id":49760014}'
    blanks = len([i for i in s[:30] if i == " "])
    s_json = json.loads(s)
    # print(s)
    s_dumped = json.dumps(s_json, separators=(",", ":"))
    # print(s_dumped)
    print("blanks: ", blanks)
    assert len(s) - len(
        s_dumped) == blanks, f"actual blanks: {blanks}\nminus  blanks: {len(s) - len(s_dumped)}\nraw: {s}\ndmp:{s_dumped}"
    id = s_json["id"]
    added_spaces = get_added_spaces(id)
    s_handled = handlePayload(s_dumped, id)
    assert len(s_handled) == len(s)
    for i in range(len(s_handled)):
        if s_handled[i] != s[i]:
            print({"i": i, "raw": s[i], "hnd": s_handled[i]})
    assert s_handled == s, f"added spaces: {added_spaces}\nminus spaces: {len(s_handled) - len(s_dumped)}\nraw:{s}\nhnd:{s_handled}"


def testSentences():
    sentences = [
        "The Robust Visual Inertial Odometry (ROVIO) algorithm [69] is another ﬁlter-based method that uses the EKF approach, and similar to other ﬁlter-based methods, it uses the IMU data to state propagation, and the camera data to ﬁlter update.",
        "However, besides per- forming the feature extraction, ROVIO executes the extraction of multi-level patches around the features, as illustrated by Figure 15.",
        "The patches are used by the prediction and update step to obtain the innovation term, i.payload_dumped., the calculation of the error between the frame and the projection of the multi-level patch into the frame.",
        "The ROVIO algorithm achieves good accuracy and robustness under a low resource utilization [18,65], being suitable for embedded implementations [65].",
        "However, the algorithm proved to be more sensitive to per-frame processing time [65] and less accurate than other algorithms, such as VI-DSO [70].",
    ]
    pass
