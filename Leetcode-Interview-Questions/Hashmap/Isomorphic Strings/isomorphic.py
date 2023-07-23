def are_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t_mapping = {}
    t_to_s_mapping = {}

    for char_s, char_t in zip(s, t):
        # Check s-to-t mapping
        if char_s in s_to_t_mapping:
            if s_to_t_mapping[char_s] != char_t:
                return False
        else:
            s_to_t_mapping[char_s] = char_t

        # Check t-to-s mapping
        if char_t in t_to_s_mapping:
            if t_to_s_mapping[char_t] != char_s:
                return False
        else:
            t_to_s_mapping[char_t] = char_s

    return True