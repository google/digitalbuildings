package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IDial;
import www.google.com.digitalbuildings._0_0_1.subfields.IResistance;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IDial_resistance_sensor extends IField{

	public IRI iri();

    public void addComposedOfDial (IDial parameter);

	public Set<IDial> getComposedOfDial();

    public void addComposedOfResistance (IResistance parameter);

	public Set<IResistance> getComposedOfResistance();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}