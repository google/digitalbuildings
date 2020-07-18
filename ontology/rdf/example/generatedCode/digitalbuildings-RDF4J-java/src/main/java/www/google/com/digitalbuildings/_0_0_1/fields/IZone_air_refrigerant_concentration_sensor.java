package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IRefrigerant;
import www.google.com.digitalbuildings._0_0_1.subfields.IZone;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.IConcentration;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IZone_air_refrigerant_concentration_sensor extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfConcentration (IConcentration parameter);

	public Set<IConcentration> getComposedOfConcentration();

    public void addComposedOfRefrigerant (IRefrigerant parameter);

	public Set<IRefrigerant> getComposedOfRefrigerant();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfZone (IZone parameter);

	public Set<IZone> getComposedOfZone();

}