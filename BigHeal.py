if not Target.HasTarget():
    if Player.Poisoned:
        Spells.CastMagery('Cure', True)
        Target.WaitForTarget(1500)
        Target.Self()
    else:
        Spells.CastMagery('Greater Heal', True)
        Target.WaitForTarget(1500)
        Target.Self()
