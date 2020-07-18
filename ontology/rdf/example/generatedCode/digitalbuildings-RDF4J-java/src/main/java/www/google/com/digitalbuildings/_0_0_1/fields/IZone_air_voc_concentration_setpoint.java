package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IZone;
import www.google.com.digitalbuildings._0_0_1.subfields.ISetpoint;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.IConcentration;
import www.google.com.digitalbuildings._0_0_1.subfields.IVoc;

public interface IZone_air_voc_concentration_setpoint extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfConcentration (IConcentration parameter);

	public Set<IConcentration> getComposedOfConcentration();

    public void addComposedOfSetpoint (ISetpoint parameter);

	public Set<ISetpoint> getComposedOfSetpoint();

    public void addComposedOfVoc (IVoc parameter);

	public Set<IVoc> getComposedOfVoc();

    public void addComposedOfZone (IZone parameter);

	public Set<IZone> getComposedOfZone();

}