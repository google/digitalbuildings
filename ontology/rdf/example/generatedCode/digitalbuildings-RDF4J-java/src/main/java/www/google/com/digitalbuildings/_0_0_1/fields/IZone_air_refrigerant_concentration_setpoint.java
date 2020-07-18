package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IRefrigerant;
import www.google.com.digitalbuildings._0_0_1.subfields.IZone;
import www.google.com.digitalbuildings._0_0_1.subfields.ISetpoint;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.IConcentration;

public interface IZone_air_refrigerant_concentration_setpoint extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfConcentration (IConcentration parameter);

	public Set<IConcentration> getComposedOfConcentration();

    public void addComposedOfRefrigerant (IRefrigerant parameter);

	public Set<IRefrigerant> getComposedOfRefrigerant();

    public void addComposedOfSetpoint (ISetpoint parameter);

	public Set<ISetpoint> getComposedOfSetpoint();

    public void addComposedOfZone (IZone parameter);

	public Set<IZone> getComposedOfZone();

}