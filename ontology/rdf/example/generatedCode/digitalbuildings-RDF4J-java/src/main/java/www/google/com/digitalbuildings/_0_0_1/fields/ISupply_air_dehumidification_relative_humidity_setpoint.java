package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IRelative;
import www.google.com.digitalbuildings._0_0_1.subfields.IDehumidification;
import www.google.com.digitalbuildings._0_0_1.subfields.IHumidity;
import www.google.com.digitalbuildings._0_0_1.subfields.ISupply;
import www.google.com.digitalbuildings._0_0_1.subfields.ISetpoint;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;

public interface ISupply_air_dehumidification_relative_humidity_setpoint extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfDehumidification (IDehumidification parameter);

	public Set<IDehumidification> getComposedOfDehumidification();

    public void addComposedOfHumidity (IHumidity parameter);

	public Set<IHumidity> getComposedOfHumidity();

    public void addComposedOfRelative (IRelative parameter);

	public Set<IRelative> getComposedOfRelative();

    public void addComposedOfSetpoint (ISetpoint parameter);

	public Set<ISetpoint> getComposedOfSetpoint();

    public void addComposedOfSupply (ISupply parameter);

	public Set<ISupply> getComposedOfSupply();

}